## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- okie
- got it
- right

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

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
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate price](avgcost:from300to700) range with [American](cuisine) food for four people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- Please find me a [low price](avgcost:less300) range restaurant in [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [bangalore](location)
- [Italian](cuisine)
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
- [less300](avgcost)
- [from300to700](avgcost)
- [more700](avgcost)
- [anyrange](avgcost)

## intent:send_email
- [yes](should_send_email)
- [no](should_send_email)
- [Yes](should_send_email)
- [No](should_send_email)
- my email id: [test@gmail.com](email_id)
- [test@gmail.com](email_id)
- email [test@gmail.com](email_id)
- mail [test@gmail.com](email_id)
 

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
- Culcatta

## synonym:Puducherry
- Pondicherry


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

## regex:pincode
- [0-9]{6}
