
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "1. 'ECHOES Koramangala' rated 4.7 with avg cost 950.  Address: 44, 4th B Cross, Koramangala 5th Block, Bangalore \n\n2. 'Windmills Craftworks' rated 4.7 with avg cost 2500.  Address: 331, EPIP Area, Road 5B, Near KTPO, Whitefield, Bangalore \n\n3. 'Toit' rated 4.6 with avg cost 2000.  Address: 298, 100 Feet Road, Namma Metro Pillar 62, Indiranagar, Bangalore \n\n4. 'Olive Bar And Kitchen' rated 4.6 with avg cost 2400.  Address: 16, Wood Street, Ashok Nagar, Richmond Road, Bangalore \n\n5. 'The London Curry House - The Royale Senate Hotel' rated 4.5 with avg cost 1700.  Address: 19/3, Kumara Krupa Road, Race Course Road, Bangalore \n\n6. 'Big Brewsky' rated 4.5 with avg cost 1800.  Address: Behind MK Retail, Before WIPRO Corporate Office, Sarjapur Road, Bangalore \n\n7. 'Byg Brewski Brewing Company' rated 4.3 with avg cost 1600.  Address: 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore \n\n8. 'Brahma Brews' rated 4.3 with avg cost 1900.  Address: Opposite Brigade Palm Springs, 24th Main, 7th Phase, JP Nagar, Bangalore \n\n9. 'URU Brewpark' rated 4.1 with avg cost 1500.  Address: Near Maratt Estate, 4th Phase, JP Nagar, Bangalore \n\n10. 'The Druid Garden' rated 4.1 with avg cost 1700.  Address: 40/1, 3rd Floor, Century Corbel Commercial, Sahakara Nagar, Bangalore \n\n"}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "lakshmi1212@gmail.com"}
    - slot{"email_id": "lakshmi1212@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"avgcost": "from300to700"}
    - slot{"avgcost": "from300to700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "1. 'Echoes Satyaniketan' rated 4.7 with avg cost 600.  Address: 17, 1st Floor, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi \n\n2. 'Big Yellow Door' rated 4.3 with avg cost 600.  Address: 2521, 2nd Floor, Kingsway Camp, Hudson Lane, GTB Nagar, New Delhi \n\n3. 'Big Yellow Door' rated 4.3 with avg cost 600.  Address: H-8 B, Near GTB Nagar Metro Station, Opposite Hudson Lane's NDPL Office, Vijay Nagar, New Delhi \n\n4. 'Chill'm Bar & Cafe' rated 4.2 with avg cost 600.  Address: 38, Bunglow Road, Kamla Nagar, New Delhi \n\n5. 'QRO Gourmeteriia BY DARK HOUSE KAFE' rated 4.2 with avg cost 600.  Address: 9, Ground Floor, Benito Juarez Marg, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi \n\n6. 'Big Yellow Door' rated 4.2 with avg cost 600.  Address: H-8, Opposite Venkateswara College, Satyaniketan, New Delhi \n\n7. 'YOLO 21' rated 4.2 with avg cost 700.  Address: 2522, Ground Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi \n\n8. 'Superstar Caf' rated 4.2 with avg cost 600.  Address: 288, Opposite Venkateshwara College, Satyaniketan, New Delhi \n\n9. 'Young Wild Free Cafe' rated 4.1 with avg cost 500.  Address: 13, 1st Floor, Opposite Venkateswara College, Satyaniketan, New Delhi \n\n10. 'Espress-o-Ville' rated 4.0 with avg cost 600.  Address: 11, Ground Floor, South Moti Bagh, Satyaniketan, New Delhi \n\n"}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "lakshmi1212"}
    - slot{"email_id": "lakshmi1212"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_re_enter_email
* send_email{"email_id": "lakshmi1212@gmail.com"}
    - slot{"email_id": "lakshmi1212@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "1. 'Pa Pa Ya' rated 4.7 with avg cost 2000.  Address: Dome, Level 4, Select Citywalk, A-3, District Centre, Saket, New Delhi \n\n2. 'Spezia Bistro' rated 4.6 with avg cost 900.  Address: 2525, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi \n\n3. 'Qubitos - The Terrace Cafe' rated 4.5 with avg cost 1500.  Address: C-7, Vishal Enclave, Opposite Metro Pillar 417, Rajouri Garden, New Delhi \n\n4. 'Ghar Bistro Cafe' rated 4.4 with avg cost 800.  Address: J-198, 2nd Floor, Rajouri Garden, New Delhi \n\n5. 'The Hudson Cafe' rated 4.4 with avg cost 850.  Address: 2524, 1st Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi \n\n6. 'Karate Kitchen' rated 4.4 with avg cost 950.  Address: Greater Kailash (GK) 1, New Delhi \n\n7. 'Locale' rated 4.4 with avg cost 1400.  Address: 17, Community Centre, Next to PVR Anupam, Saket, New Delhi \n\n8. 'Rajinder Da Dhaba' rated 4.3 with avg cost 800.  Address: AB 14, Safdarjung Enclave Market, Safdarjung, New Delhi \n\n9. 'Local' rated 4.3 with avg cost 1600.  Address: 11, KG Marg, Scindia House, Connaught Place, New Delhi \n\n10. 'Tamra - Shangri-La's - Eros Hotel' rated 4.3 with avg cost 3800.  Address: Shangri-La's Eros Hotel, 19, Ashoka Road, Janpath, New Delhi \n\n"}
    - utter_ask_send_email
* send_email{"should_send_email": "no"}
    - slot{"should_send_email": "no"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
 

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
#########DONE##########

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "abcd"}
    - slot{"location": "abcd"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"avgcost": "from300to700"}
    - slot{"avgcost": "from300to700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "1. 'Echoes Satyaniketan' rated 4.7 with avg cost 600.  Address: 17, 1st Floor, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi \n\n2. 'Food Scouts' rated 4.6 with avg cost 700.  Address: Punjabi Bagh, New Delhi \n\n3. 'Food Scouts' rated 4.4 with avg cost 700.  Address: Near TDI Mall, Rajouri Garden, New Delhi \n\n4. 'Food Scouts' rated 4.3 with avg cost 700.  Address: Janakpuri, New Delhi \n\n5. 'Punjabi Angithi' rated 4.3 with avg cost 400.  Address: 32-22, A 4, DDA Market, Paschim Vihar, New Delhi \n\n6. 'QRO Gourmeteriia BY DARK HOUSE KAFE' rated 4.2 with avg cost 600.  Address: 9, Ground Floor, Benito Juarez Marg, Opposite Sri Venkateshwara College, Satyaniketan, New Delhi \n\n7. 'Dilli Treat' rated 4.2 with avg cost 500.  Address: 3/80, Shankar Road, Old, Rajinder Nagar, New Delhi \n\n8. 'Chill'm Bar & Cafe' rated 4.2 with avg cost 600.  Address: 38, Bunglow Road, Kamla Nagar, New Delhi \n\n9. 'London Street Kitchen' rated 4.2 with avg cost 600.  Address: 4A-59, Old, Rajinder Nagar, New Delhi \n\n10. 'Indus Flavour' rated 4.1 with avg cost 700.  Address: 2510, Ground Floor, Hudson Lane, Kingsway Camp, Delhi University-GTB Nagar, New Delhi \n\n"}
    - utter_ask_send_email
* send_email{"should_send_email": "no"}
    - slot{"should_send_email": "no"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
