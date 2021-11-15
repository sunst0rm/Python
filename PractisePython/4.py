#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


number = int(input("Enter a number: "))

new_list = range(1, number+1)

xList = []

for x in new_list:
    if number % x == 0:
        xList.append(x)

print(xList)