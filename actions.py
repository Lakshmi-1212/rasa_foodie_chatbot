from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted
import pandas as pd
import json

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

def get_average_cost_range(AvgCostFor2):
	min_cost = 0
	max_cost = 999999 #arbitrary max value
	if AvgCostFor2 is not None:
		if (AvgCostFor2 == "less300"):
			max_cost = 300
		elif (AvgCostFor2 == "from300to700"):
			min_cost = 300
			max_cost = 700
		elif (AvgCostFor2 == "more700"):
			min_cost = 700

	print(f'4DEBUG - get_average_cost_range {min_cost},{max_cost}')
	return min_cost,max_cost

def check_city_validity(city):
	return True if city in WeOperate else False



def RestaurantSearch(City,Cuisine,AvgCostFor2):
	min_cost, max_cost = get_average_cost_range(AvgCostFor2)


	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower()))
					  &
					  (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))
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
		print(f"4DEBUG - City: {loc},Cuisine: {cuisine}, Cost for two:{avgcost}")
		results = RestaurantSearch(City=loc,Cuisine=cuisine,AvgCostFor2=avgcost)
		response=""
		results_found = False
		if results.shape[0] == 0:
			response= f"No results found for City: {loc},Cuisine: {cuisine}, Cost for two:{avgcost}"
		else:
			# Sort restaurants based on their ratings
			results_found = True
			rest_count = 1
			# print(f"4DEBUG - results:{results}")
			results.sort_values(by=['Aggregate rating'], axis=0, ascending=False, inplace=True)
			#for restaurant in RestaurantSearch(loc,cuisine).iloc[:5].iterrows():

			response = response + \
					   f"Top rated {cuisine} restaurants in {loc} \n\n"
			for index, restaurant in results.head(5).iterrows():
				# for restaurant in results.iloc[:5].iterrows():
				# restaurant = restaurant[1]
				response = response + \
						   f"{rest_count}. '{restaurant['Restaurant Name']}' " \
						   f"rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']}. " \
						   f" Address: {restaurant['Address']} \n\n"

				rest_count += 1
		print(f"4DEBUG:{response}")
		dispatcher.utter_message(response)
		return [SlotSet('results_found',results_found)]


def sendmail(receiver_mail_id, location):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	mail_content = "Hello,\n" \
				   "This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.\n" \
				   "Thank You"


	# The mail addresses and password


	sender_address = 'foodie.restaurant.chatbot@gmail.com'
	sender_pass = 'foodiechatbot'
	receiver_address = receiver_mail_id
	# Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = f'Foodie Chatbot TESTING: Top rated restaurants in {location}'  # The subject line
	# The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	# Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
	session.starttls()  # enable security
	session.login(sender_address, sender_pass)  # login with mail_id and password
	text = message.as_string()
	print(f'4DEBUG: Sending email, from:{sender_address}, to:{receiver_address}')
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')

class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		receiver_email_id = tracker.get_slot('email_id')

		location = tracker.get_slot('location')

		print(f"4DEBUG: Before sending mail. To: {receiver_email_id}, city:{location}")

		sendmail(receiver_email_id,location)
		return [SlotSet('email_id',receiver_email_id)]

def check_mail(email_id):
	return True

class ActionCheckMail(Action):
	def name(self):
		return 'action_check_email'

	def run(self, dispatcher, tracker, domain):
		receiver_email_id = tracker.get_slot('email_id')

		valid_email = check_mail(receiver_email_id)
		print(f'4DEBUG: email validity: email {receiver_email_id} - {valid_email}')

		return [SlotSet('is_valid_email',valid_email)]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_loc'

	def run(self, dispatcher, tracker, domain):
		city = tracker.get_slot('location')

		## DEBUG - BEGIN

		#loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		avgcost = tracker.get_slot('avgcost')
		print(f"4DEBUG checklocation - City: '{city}',Cuisine: {cuisine}, Cost for two:{avgcost}")
		## DEBUG - END

		city_validity = check_city_validity(city)
		print(f'4DEBUG: city validity: City {city} - {city_validity}')

		if not city_validity:
			response = f"Sorry!! We do not support this region currently!!"
			dispatcher.utter_message(response)
		return [SlotSet('is_valid_city',city_validity)]

class ActionRestarted(Action):
	def name(self):
		return "action_chat_restart"

	def run(self, dispatcher, tracker, domain):
		return [Restarted()]