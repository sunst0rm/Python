# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Please give a number "))
check = int(input("Please give a second number "))

if num % 4 == 0:
    print("Number multiplies by 4")
elif num % 2 == 0:
    print("Number is even")
else:
    prnt("Number is odd")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)