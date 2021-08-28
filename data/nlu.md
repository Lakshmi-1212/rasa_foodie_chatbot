

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hallo
- hi
- hello
- Hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- Eating joints
- I am searching for a dinner spot
- i want to know few restaurants
- search for places to eat
- Food places to eat
- I want to eat
- restaurants in [bangalore](location)
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- I’m hungry. Looking out for some good restaurants
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in [chennai](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in [bangalore](location)
- I am looking for [south indian](cuisine) food
- in [Gurgaon](location)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- in [mubaim](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [Mexican](cuisine)
- can you book a table in [chennai](location) in a [moderate price](avgcost:from300to700) range with [American](cuisine) food for four people
- Find restaurants in [chennai](location) in a [low price](avgcost:less300) range with [North Indian](cuisine) food  
- [Bangalore](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- Please find me a [low price](avgcost:less300) range restaurant in [bangalore](location)
- [mumbai](location)
- show me restaurants
- [bangalore](location) 
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [South Indian](cuisine) with a price range below [Rs. 300](avgcost)
- Average cost above [Rs. 700](avgcost)
- Cost for two between [Rs. 300 to Rs. 700](avgcost)
- Cost is below [Rs. 300](avgcost)
- Price range is below [Rs. 300](avgcost)
- Can you suggest some good restaurants in [kolkata](location)
- I’m hungry. Looking out for some good restaurants
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- Search for [North Indian](cuisine) restaurants in [delhi](location)
- Search for restaurants in [Bangalore](location) with price range [less than 300](less300)
- Want to know about restaurants in [Bangalore](location) with cost for two between [more than Rs.700](avgcost)
- Restaurants in [Delhi](location) at [any price](avgcost) range
- Okay. Show me some in [Allahabad](location)
- [allahabad](location)
- in [delhi](location) for [North Indian](cuisine) cuisine

## intent:send_email
- [send_email](should_send_email)
- [dont_send_email](should_send_email)
- [send email](should_send_email:send_email)
- [Yes, send email](should_send_email:send_email)
- [dont send email](should_send_email:dont_send_email)
- [No, dont send email](should_send_email:dont_send_email)
- my email id: [test@gmail.com](email_id)
- [test@gmail.com](email_id)
- email [test@gmail.com](email_id)
- mail [test@gmail.com](email_id)
- Please send it to [test@gmail.com](email_id)
- Send email to [test@gmail.com](email_id)
- this is my email id  [test@gmail.com](email_id)
- here it is [test@gmail.com](email_id)
- send mail to [test@gmail.com](email_id)
- mail to [test@gmail.com](email_id)
- email [test@gmail.com](email_id)
- mail [test@gmail.com](email_id)
- my email id is [test@gmail.com](email_id)
- here you go [test@gmail.com](email_id)

 

## synonym:New Delhi
- Delhi

## synonym:bangalore
- Bengaluru
- Blore

## synonym:Mysore
- Mysuru

## synonym:Chennai
- Madras


## synonym:Kochi
- Cochin


## synonym:Kolkata
- Calcutta

## synonym:Puducherry
- Pondicherry
- Pondy
- Pondi


## synonym:Kanpur
- Cawnpore

## synonym:Guwahati 
- Gauhati  

## synonym:Indore
- Indhur

## synonym:Pune
- Poona

## synonym:Shimla
- Simla

## synonym:Varanasi
- Benares

## synonym:Vizag
- Visakhapatnam
- Waltair

## synonym:Mangaluru
- Mangalore


## synonym:Varanasi
- Benares

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:greet
- hey[^\s]*
