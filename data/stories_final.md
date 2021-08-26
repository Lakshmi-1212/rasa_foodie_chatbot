## Complete happy path
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
    - slot{"email_contents": "email-contents-top rated restaurants"}
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
    - utter_restart
    - action_chat_restart
    
## Happy path - first invalid email
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
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "test123"}
    - slot{"email_id": "test123"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_re_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
    
 ## Happy path - twice invalid email - stop
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
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "test123"}
    - slot{"email_id": "test123"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_re_enter_email
* send_email{"email_id": "test"}
    - slot{"email_id": "test"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
 
## Without email
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
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "no"}
    - slot{"should_send_email": "no"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found
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
    
######
## First time invalid city (TODO FOR ALL COMBINATIONS)

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
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "no"}
    - slot{"should_send_email": "no"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## Complete happy path - First time invalid city
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
    - slot{"email_contents": "email-contents-top rated restaurants"}
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
    - utter_restart
    - action_chat_restart
    
## Happy path - first invalid email- First time invalid city
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
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"avgcost": "from300to700"}
    - slot{"avgcost": "from300to700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "test123"}
    - slot{"email_id": "test123"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_re_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
    
 ## Happy path - First time invalid city- twice invalid email - stop
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
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"avgcost": "from300to700"}
    - slot{"avgcost": "from300to700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "yes"}
    - slot{"should_send_email": "yes"}
    - utter_enter_email
* send_email{"email_id": "test123"}
    - slot{"email_id": "test123"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_re_enter_email
* send_email{"email_id": "test"}
    - slot{"email_id": "test"}
    - action_check_email
    - slot{"is_valid_email": false}
    - utter_invalid_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
 
## Without email- First time invalid city
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
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "no"}
    - slot{"should_send_email": "no"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found- First time invalid city
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
    