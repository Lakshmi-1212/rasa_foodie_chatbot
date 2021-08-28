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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
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
## First time invalid city 

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
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
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
    
## ##### 
    
## Complete happy path- user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "bangalore"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## Happy path - first invalid email - user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "bangalore"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
    
    
 ## Happy path - twice invalid email - stop - user query with all entities together
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "bangalore"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
 
## Without email - user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "bangalore"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found - user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "bangalore"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
######
## First time invalid city  - don't send email - user query with all entities together

* greet
    - utter_greet
* restaurant_search{"location": "abcd", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## First time invalid city - send email - user query with all entities together
* greet
    - utter_greet
    
* restaurant_search{"location": "abcd", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## First time invalid city - first invalid email- user query with all entities together
* greet
    - utter_greet
    
* restaurant_search{"location": "abcd", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
    
    
 ## Happy path - First time invalid city- twice invalid email - stop - user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "abcd", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
 
## Without email- First time invalid city - user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "abcd", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found- First time invalid city - user query with all entities together
* greet
    - utter_greet
* restaurant_search{"location": "abcd", "avgcost": "from300to700", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - slot{"avgcost": "from300to700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_results_not_found
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
    
## ##########   
    
## Complete happy path- user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## Happy path - first invalid email - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
    
    
 ## Happy path - twice invalid email - stop - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
 
## Without email - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": true}  
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
######
## First time invalid city  - don't send email - user query with cuisine & city together

* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## First time invalid city - send email - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## First time invalid city - first invalid email- user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
    
    
 ## Happy path - First time invalid city- twice invalid email - stop - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
 
## Without email- First time invalid city - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found- First time invalid city - user query with cuisine & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "abcd"}
    - utter_ask_budget
* restaurant_search{"avgcost": "more700"}
    - slot{"avgcost": "more700"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_results_not_found
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## ##############
## City and avgcost together

    
## Complete happy path- user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"avgcost": "less300", "location": "chandigarh"}
    - slot{"avgcost": "less300"}
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## Happy path - first invalid email - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"avgcost": "less300", "location": "chandigarh"}
    - slot{"avgcost": "less300"}
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
    
    
 ## Happy path - twice invalid email - stop - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"avgcost": "less300", "location": "chandigarh"}
    - slot{"avgcost": "less300"}
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
 
## Without email - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"avgcost": "less300", "location": "chandigarh"}
    - slot{"avgcost": "less300"}
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": true}  
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"avgcost": "less300", "location": "chandigarh"}
    - slot{"avgcost": "less300"}
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
######
## First time invalid city  - don't send email - user query with average cost & city together

* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - slot{"location": "abcd"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": false}
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## First time invalid city - send email - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - slot{"location": "abcd"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## First time invalid city - first invalid email- user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - slot{"location": "abcd"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
    
    
 ## Happy path - First time invalid city- twice invalid email - stop - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - slot{"location": "abcd"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
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
 
## Without email- First time invalid city - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - slot{"location": "abcd"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true} 
    - action_search_restaurants
    - slot{"results_found": true}
    - slot{"email_contents": "email-contents-top rated restaurants"}
    - utter_ask_send_email
* send_email{"should_send_email": "dont_send_email"}
    - slot{"should_send_email": "dont_send_email"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## restaurant search - results not found- First time invalid city - user query with average cost & city together
* greet
    - utter_greet
* restaurant_search{"location": "abcd",  "avgcost": "less300"}
    - slot{"avgcost": "less300"}
    - slot{"location": "abcd"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_loc
    - slot{"is_valid_city": false} 
    - utter_we_dont_operate
    - utter_enter_loc_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_loc
    - slot{"is_valid_city": true}
    - action_search_restaurants
    - slot{"results_found": false}
    - slot{"email_contents": ""}
    - utter_results_not_found
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
    
######
## Happy Path again

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - utter_goodbye
    - utter_restart
    - action_chat_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
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
* send_email{"should_send_email": "send_email"}
    - slot{"should_send_email": "send_email"}
    - utter_enter_email
* send_email{"email_id": "test@gmail.com"}
    - slot{"email_id": "test@gmail.com"}
    - action_check_email
    - slot{"is_valid_email": true}
    - action_send_email
    - slot{"email_id": "test@gmail.com"}
    - utter_goodbye
    - utter_restart
    - action_chat_restart

######