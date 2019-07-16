#Krish Patel
#Wednesday September 19, 2018
#This program will be capable of recommending regions of Canada to visit based on your preferences




#If the password is correct, Python asks the user 3-4 questions on their preferences

opinion_on_Canada=input("Do you like the great country, Canada?(Yes/No)")
if(opinion_on_Canada=="Yes" or opinion_on_Canada=="No"):
    print("Noted! Lets continue. In advance, if the code does not run, you may have mispelled an answer. So it try again!")

    #Asks user questions on their geological preferences
    Q1_climate=input("Do you prefer a warmer or colder climate?[TYPE 'warmer' or 'colder'")
    Q2_region=input("Do you prefer a urban or rural region?[TYPE 'urban' or 'rural'")
    Q3_monuments=input("Do you enjoy viewing monuments or historical buildings?[TYPE 'Yes' or 'No'")
    
    #If the user answeres Q1_climate with "colder", Python asks the user if they also like mountains
    if(Q1_climate=="colder"): 
        Q4_mounatins=input("Do you enjoy mountains?[TYPE 'Yes' or 'No'")
    else:
        print("")
    #These are the many combinations of where the user would be suggested based on their answers

    #If the user answered in this combination, the user will be suggested to go to Ottawa
    if(Q1_climate=="warmer" and Q2_region=="urban" and Q3_monuments=="Yes"):
        print("I suggest you travel to Ottawa")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane, Foot or Train?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 4H 20min drive and is 449km from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is about 500km, will be a 55min ride and will cost $360 for a roundtrip from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 384KM walk and will take 78H from Richmond Hill")
        elif(mode_of_travel=="Train"):
            print("You are crazy! That is a 4H 52 ride and will cover about 400KM from Richmond Hill")

    #If the user answered in this combination, the user will be suggested to go to Blue Mountain
    elif(Q1_climate=="colder" and Q2_region=="urban" and Q3_monuments=="Yes" and Q4_mounatins=="Yes"):
        print("I suggest you travel to Blue Mountain")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 1.58H drive and is 157km from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 137KM walk and will take 28H from Richmond Hill")

    #If the user answered in this combination, the user will be suggested to go to Newfoundland
    elif(Q1_climate=="warmer" and Q2_region=="rural" and Q3_monuments=="Yes"):
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        print("I suggest Newfoundland ")
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 35 drive and is 2,736km away from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is 2,736km, will be a 2H 55 min ride from Richmond Hill and will cost $704")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 2,736KM walk from Richmond Hill and will take 438H")

    #If the user answered in this combination, the user will be suggested to go to Salluit, Quebec
    elif(Q1_climate=="colder" and Q2_region=="rural" and Q3_monuments=="Yes" and Q4_mounatins=="No"):
        print("I suggest you travel to Salluit, Quebec which is 2070km")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 2070km ride from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is 2,070km from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 2,070KM walk from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to British Columbia
    elif(Q1_climate=="warmer" and Q2_region=="urban" and Q3_monuments=="No"):
        print("I suggest Bell II, British Columbia")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 35 drive and is 2,736km away from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is 2,736km and will be a 2H 55 min ride from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 2,736KM walk and will take 438H from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to Banff, BC
    elif(Q1_climate=="warmer" and Q2_region=="urban" and Q3_monuments=="No"):
        print("I suggest Banff")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 34 drive and is 3,560km away from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is about 3,200km and will be a 4H 10 min ride from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 3,328KM walk and will take 659H from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to Gros Morne National Park
    elif(Q1_climate=="warmer" and Q2_region=="rural" and Q3_monuments=="No"):
        print("I suggest Gros Morne National Park")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 31 drive and is 2,481km away from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is about 3,200km and will be a 2H 35 min ride from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 2,392KM walk and will take 375H from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to Whistler Mountain
    elif(Q1_climate=="colder" and Q2_region=="rural" and Q3_monuments=="Yes" and Q4_mounatins=="Yes"):
        print("I suggest Whistler Mountain")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot? from Richmond Hill")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 42 drive and is 4,506km away from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is about 4,500km from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to Mt. St Louis
    elif(Q1_climate=="colder" and Q2_region=="urban" and Q3_monuments=="No" and Q4_mounatins=="Yes"):
        print("I suggest Mt. St Louis")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Bus or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 1H 34min drive and is 140 km away from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 122KM walk and will take 25H from Richmond Hill")

    #If the user answered in this combination, the user will be suggested to go to Sunshine Village
    elif(Q1_climate=="colder" and Q2_region=="rural" and Q3_monuments=="No" and Q4_mounatins=="Yes"):
        print("I suggest Sunshine Village")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Bicycle or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 34H drive and is 3,574 km away from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 3,380KM walk and will take 672H from Richmond Hill")
        elif(mode_of_travel=="Bicycle"):
            print("Wow,  that is a 3,554KM ride and will take 178H from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to New Brunswick
    elif(Q1_climate=="colder" and Q2_region=="urban" and Q3_monuments=="No" and Q4_mounatins=="No"):
        print("I suggest New Brunswick")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 13H 44min drive and is 1,358 km away from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 1,258KM walk and will take 258H from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("Wow, that is a 1,258KM ride and will take 2H 20m from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to PEI
    elif(Q1_climate=="colder" and Q2_region=="rural" and Q3_monuments=="No" and Q4_mounatins=="No"):
        print("I suggest Prince Edward Island")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane or Foot? from Richmond Hill")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 16H 24min drive and is 1,686 km away from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 1,707KM walk and will take 344H from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is a about 1,700KM ride and will take 2H from Richmond Hill")
            
    #If the user answered in this combination, the user will be suggested to go to Vancouver
    elif(Q1_climate=="colder" and Q2_region=="urban" and Q3_monuments=="Yes" and Q4_mounatins=="No"):
        print("I suggest you travel to Vancouver")
        #Asks user which mode of transportation they will use if they go to the suggested location and informs the user of how far in KM it is and how long it will take to travel there using the mode of transporation
        mode_of_travel=input("Will you be travelling by Car,Airplane, Foot or Bus?")
        if(mode_of_travel=="Car"):
            print("Woah! That is a 42H drive and is 42,291km from Richmond Hill")
        elif(mode_of_travel=="Airplane"):
            print("That is 42,291km and will be a 4H 45min ride from Richmond Hill")
        elif(mode_of_travel=="Foot"):
            print("You are crazy! That is a 4,041KM walk and will take 812H from Richmond Hill")
        elif(mode_of_travel=="Bus"):
            print("You are crazy! That is a 2 day and 18H ride and will cover about 4,000KM from Richmond Hill")

elif(opinion_on_Canada!="Yes" or opinion_on_Canada!="No"):
#If the user does not answer with 'Yes' or 'No' Python reminds them of the two options
    print("Try again, but answer with 'Yes' or 'No'") 


