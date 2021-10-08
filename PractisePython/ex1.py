# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


import datetime                                     #Imports datetime library

now = datetime.datetime.now()                       #Defines now class(?)

name = input("What is your name? ")                 #Asks user to enter name

age = int(input("What is your age? "))              #Asks to enter their age

year = (now.year + 100) - age                       #Defines year argument

msg = name + " in 100 years you will be: ", year    #Tells in which year they will be 100 years old

print(msg)                                          #Prints it

n = int(input("Please provide a number: "))         #Ask about a number

print(msg * n)                                      #Prints it
