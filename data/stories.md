## complete path - happy path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - action_chat_restart
    - utter_restart
