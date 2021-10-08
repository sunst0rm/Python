def check_user_input(input):                                                # defines a function
    try:
        val = int(input)                                                    # int() converts input to integer
        print("Input is an integer. You typed = ", val)                     # prints a message if all good
    except ValueError:                                                      # defines confition if not good
        print("No.. input is not a number, it's a string")


input1 = input("Please specify any number ")                                #
check_user_input(input1)



