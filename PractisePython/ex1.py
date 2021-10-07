# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Asks use to enter name
name = input("What is your name? ")
print("Ok thanks sir, so your name is " + name)

#Asks to enter their age
age = int(input("What is your age? "))
print("Ok sir so your age is: ", age)

year = str((2021 + age)+100)

#Tells in which year they will be 100 years old
print(name + " in 100 years you will be: ", year)