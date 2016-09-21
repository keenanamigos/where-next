#!/usr/bin/python
import random

domestic = "./destinations/us-destinations.txt" #stores the domestic locations
international = "./destinations/intl-destinations.txt" #stores the international locations
holiday = "./destinations/2016-holiday.txt" #stores the holiday locations

#Get Input
travel = raw_input("Travel domestically, internationally, or on a holiday trip for your next adventure? Please enter 'domestic', 'international', or 'holiday': ")
travel = travel.lower()

#Validate Input
while travel not in {'domestic', 'international', 'holiday'}:
    print("\n")
    print ("Invalid input. Please enter 'domestic', 'international', or 'holiday' to continue.")
    print("\n")
    travel = raw_input("Would you like to travel domestically, internationally, or on a holiday trip for your next adventure? Please enter 'domestic', 'international', or 'holiday': ")
    travel = travel.lower()

#Get Domestic Locations        
if (travel == 'domestic'):
    file_obj = open(domestic,'r')
    random_domestic = random.choice(file_obj.readlines())
    file_obj.close()
    print ("Your next adventure should be to: " + random_domestic)
#Get International Locations    
elif (travel == 'international'):
    file_obj = open(international,'r')
    random_intl = random.choice(file_obj.readlines())
    file_obj.close()
    print ("Your next adventure should be to: " + random_intl)
#Get 2016 Holiday Locations
elif (travel == 'holiday'):
    file_obj = open(holiday, 'r')
    random_holiday = random.choice(file_obj.readlines())
    file_obj.close()
    print ("Take your holiday this year to: " + random_holiday)
