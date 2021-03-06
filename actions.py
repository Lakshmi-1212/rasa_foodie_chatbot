from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted
import pandas as pd
import json
import re
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)

# From default file shared
#WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']


# Tier 1 & 2 cities from the link
# Tier1_Cities = ['Ahmedabad','Bengaluru','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune']
# Tier2_Cities = ['Agra','Ajmer','Aligarh','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bilaspur','BokaroSteelCity','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad','Bhilai','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur','Gwalior','Gurgaon','Guwahati','Hamirpur','Hubli–Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jalgaon','Jammu','Jamnagar','Jamshedpur','Jhansi','Jodhpur','Kakinada','Kannur','Kanpur','Karnal','Kochi','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow','Madurai','Malappuram','Mathura','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida','Patna','Pondicherry','Purulia','Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Ratlam','Salem','Sangli','Shimla','Siliguri','Solapur','Srinagar','Surat','Thanjavur','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruvannamalai','Ujjain','Bijapur','Vadodara','Varanasi','Vasai-VirarCity','Vijayawada','Visakhapatnam','Vellore','Warangal']
# WeOperate = Tier1_Cities + Tier2_Cities

# Distinct city names from zomato.csv file (Link has Bengaluru and csv has Bangalore. Hence using below list which matches zomato.csv)
WeOperate = ['Agra', 'Ahmedabad', 'Allahabad', 'Amritsar', 'Aurangabad',
       'Bangalore', 'Bhopal', 'Bhubaneshwar', 'Chandigarh', 'Chennai',
       'Coimbatore', 'Dehradun', 'Faridabad', 'Gangtok', 'Ghaziabad',
       'Goa', 'Gurgaon', 'Guwahati', 'Hyderabad', 'Indore', 'Jaipur',
       'Kanpur', 'Kochi', 'Kolkata', 'Lucknow', 'Ludhiana', 'Mangalore',
       'Mohali', 'Mumbai', 'Mysore', 'Nagpur', 'Nashik', 'Nasik',
       'New Delhi', 'Noida', 'Ooty', 'Panchkula', 'Patna', 'Puducherry',
       'Pune', 'Ranchi', 'Secunderabad', 'Shimla', 'Surat', 'Vadodara',
       'Varanasi', 'Vizag']

WeOperate_lower = [city.lower() for city in WeOperate]

# Set default cuisine in case it is not picked
DEFAULT_CUISINE = 'Chinese'

# email regular expressions to validate and extract email id
# Slack sends email id as 'mailto:test@gmail.com|test@gmail.com'
EMAIL_REGEX = '[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+'
EMAIL_MAILTO_REGEX = f'^(mailto:{EMAIL_REGEX}\|)?({EMAIL_REGEX}$)'  # To handle slack email string

def get_average_cost_range(avgCostFor2):
	min_cost = 0
	max_cost = 50000 #arbitrary max value - found max of 8000 in zomato.csv
	if avgCostFor2 is not None:
		if (avgCostFor2 == "less300"):
			max_cost = 300
		elif (avgCostFor2 == "from300to700"):
			min_cost = 300
			max_cost = 700
		elif (avgCostFor2 == "more700"):
			min_cost = 700

	print(f'Min & max price range for 2: {min_cost},{max_cost}')
	return min_cost,max_cost

def check_city_validity(city):
	return True if city.lower() in WeOperate_lower else False


class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_loc'

	def run(self, dispatcher, tracker, domain):
		city = tracker.get_slot('location')

		city_validity = check_city_validity(city)
		print(f'City validity: City {city} - {city_validity}')

		return [SlotSet('is_valid_city',city_validity)]

def RestaurantSearch(city,cuisine,avgCostFor2):
	min_cost, max_cost = get_average_cost_range(avgCostFor2)


	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: cuisine.lower() in x.lower()))
					  &
					  (ZomatoData['City'].apply(lambda x: city.lower() in x.lower()))
					  &
					  (ZomatoData['Average Cost for two'] > min_cost)
					  &
					  (ZomatoData['Average Cost for two'] <= max_cost)
					]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		avgcost = tracker.get_slot('avgcost')
		print(f"Search Restaurants: City: {loc}(valid_city - {tracker.get_slot('is_valid_city')}),"
			  f"Cuisine: {cuisine}, Cost for two:{avgcost}")

		if cuisine is None:
			dispatcher.utter_message(f"Cuisine not set. Choosing for default cuisine: {DEFAULT_CUISINE}")
			cuisine = DEFAULT_CUISINE


		results = RestaurantSearch(city=loc,cuisine=cuisine,avgCostFor2=avgcost)
		response=""
		email_contents = ""
		results_found = False
		if results.shape[0] == 0:
			response= f"No results found for City: {loc},Cuisine: {cuisine}, Cost for two:{avgcost}"
		else:
			# Sort restaurants based on their ratings
			results_found = True
			results.sort_values(by=['Aggregate rating'], axis=0, ascending=False, inplace=True)

			# Output response - top 5 rated restaurants
			rest_count = 1
			response = response + \
					   f"\nTop rated {cuisine} restaurants in {loc} \n     \n"
			for index, restaurant in results.head(5).iterrows():
				response = response + \
						   f"{rest_count}. '{restaurant['Restaurant Name']}' " \
						   f"rated {restaurant['Aggregate rating']} with an average cost for two: {restaurant['Average Cost for two']}. " \
						   f" Address: {restaurant['Address']} \n     \n"

				rest_count += 1

			### EMAIL CONTENTS - top 10 rated restaurants
			rest_count = 1
			for index, restaurant in results.head(10).iterrows():
				email_contents = email_contents + \
						   f"{rest_count}. '{restaurant['Restaurant Name']}' " \
						   f"rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']}. " \
						   f" Address: {restaurant['Address']} \n\n"
				rest_count += 1

		dispatcher.utter_message(response)
		return [SlotSet('results_found',results_found),SlotSet('email_contents',email_contents)]





def create_send_email(sender_address, sender_password, receiver_address, text):
	print(f"Thread: Sending email to:{receiver_address}")
	# Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
	session.starttls()  # enable security
	session.login(sender_address, sender_password)  # login with mail_id and password
	session.sendmail(sender_address, receiver_address, text)
	session.quit()

	print(f"Thread: email sent to {receiver_address}")

def sendmail(receiver_mail_id, location, email_contents):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	mail_content = email_contents if email_contents is not None else "No restaurants found"

	# The mail address and password
	sender_address = 'foodie.restaurant.chatbot@gmail.com'
	sender_pass = 'foodiechatbot'
	receiver_address = receiver_mail_id


	print(f'Sending email, from:{sender_address}, to:{receiver_address}')

	# Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = f'Foodie Chatbot: Top rated restaurants in {location}'  # The subject line
	# The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	text = message.as_string()

	# NOTE: rasa times out after 10 seconds (default setting in rasa package) if it does not receive a response for an action
	# Due to this, rasa was getting hung while sending emails
	# Two options to resolve this issue:
	# 1. Change the default timeout either in the package (console.py) or invoke rasa shell with parameter --response-timeout
	# 2. Make the process of sending email asynchronous.
	# We have implemented option 2 here and used threads to send out email & rasa does not timeout due to server delays
	t = threading.Thread(target=create_send_email, args=[sender_address, sender_pass, receiver_address, text])
	t.daemon = True
	t.start()

	# create_send_email(sender_address, sender_pass, receiver_address, text)

	print(f'Mail sent to:{receiver_address}')

class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		receiver_email_id = tracker.get_slot('email_id')

		# Check if email id is from slack
		if(receiver_email_id.startswith('mailto')):
			result = re.search(EMAIL_MAILTO_REGEX, receiver_email_id)
			receiver_email_id = result.group(2)


		location = tracker.get_slot('location')
		email_contents = tracker.get_slot('email_contents')

		#dispatcher.utter_message(f'Sending e-mail to:{receiver_email_id	}')

		sendmail(receiver_email_id,location, email_contents)

		response = f'Mail sent to {receiver_email_id}'
		dispatcher.utter_message(response)

		return [SlotSet('email_id',receiver_email_id)]

def check_mail(email_id):
	return True if(re.search(EMAIL_MAILTO_REGEX,email_id)) else False



class ActionCheckMail(Action):
	def name(self):
		return 'action_check_email'

	def run(self, dispatcher, tracker, domain):
		receiver_email_id = tracker.get_slot('email_id')

		valid_email = check_mail(receiver_email_id)
		print(f'Checking email validity: email {receiver_email_id} - {valid_email}')

		return [SlotSet('is_valid_email',valid_email)]


class ActionRestarted(Action):
	def name(self):
		return "action_chat_restart"

	def run(self, dispatcher, tracker, domain):
		return [Restarted()]