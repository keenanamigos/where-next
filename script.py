#!/usr/bin/python
import random

domestic = "./destinations/us-destinations.txt" #stores the domestic locations
international = "./destinations/intl-destinations.txt" #stores the international locations

#Get Input
travel = raw_input("Would you like to travel domestically or internationally for your next adventure? Please enter 'domestic' or 'international': ")
travel = travel.lower()

#Validate Input
while travel not in {'domestic', 'international'}:
    print("\n")
    print ("Invalid input. Please enter 'domestic' or 'international' to continue.")
    print("\n")
    travel = raw_input("Would you like to travel domestically or internationally for your next adventure? Please enter 'domestic' or 'international': ")
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