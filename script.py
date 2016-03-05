#!/usr/bin/python
import random

domestic = "./destinations/us-destinations.txt" #stores the domestic locations
international = "./destinations/intl-destinations.txt" #stores the international locations

travel = input("Would you like to travel domestically or internationally for your next adventure? Please enter 'domestic' or 'international': ")
        
if (travel == 'domestic'):
    file_obj = open(domestic,'r')
    random_domestic = random.choice(file_obj.readlines())
    file_obj.close()
    print ("Your next adventure should be to: " + random_domestic)
elif (travel == 'international'):
    file_obj = open(international,'r')
    random_intl = random.choice(file_obj.readlines())
    file_obj.close()
    print ("Your next adventure should be to: " + random_intl)