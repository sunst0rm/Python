# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

x = int(input("Please type a number "))

if (x % 2) == 0:
    print("Number is even")
else:
    print("Number is odd")