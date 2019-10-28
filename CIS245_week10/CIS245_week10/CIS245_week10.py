"""
Name: Assignment 10.1
Programmer: Jacob Hayes
Date: 28 Oct 2019
Purpose: Perform basic file processing
"""

#------------------------------------------------------------------------#
################################DEPENDENCIES##############################
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
##################################IMPORTS#################################
#------------------------------------------------------------------------#

import os #to edit files
import sys #to exit

#------------------------------------------------------------------------#
##################################CLASSES#################################
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
#################################FUNCTIONS################################
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
###################################MAIN###################################
#------------------------------------------------------------------------#
file_path = ''

#loop until they give us a directory that exists
while os.path.isdir(file_path) == False:
    file_path = input("What directory would you like to write to? ")

#find the file name the user wants to write to
file_name = input("What is the name of the file you'd like to write? ")

#append the file name to the file path
file_path += "/" + file_name

#gather data to write to the file
name = input("What is your name? ")
address = input("What is your address? ")
phone = input("What is your phone number? ")

#log_output holds our output to the file
log_output = name + "," + address + "," + phone

#attempt to open the file path for writing, creating it if it doesn't exist and throwing an error if we can't write to it
try:
    with open(file_path, 'w+') as fileHandle:
        fileHandle.write(log_output)
except:
    #we coudln't write to the file for some reason - let the user know and quit the program
    print("An error occurred. Check that you have permission to write to that location and try again.")
    input("Press Enter to continue...")
    os._exit(1)

#open the file in order to read what's inside
with open(file_path, 'r') as fileHandle:
    log_input = fileHandle.readline()

    #find the separators
sep1 = log_input.find(',')
sep2 = log_input.find(',', sep1 + 1)

#assign the substrings (separated by the sep values) to new variables to show that we are correctly reading data from the file
name_ = log_input[0: sep1]
address_ = log_input[sep1 + 1: sep2]
phone_ = log_input[sep2 + 1:]

#print the output to the console
print("Name: " + name_)
print("Address: " + address_)
print("Phone: " + phone_)