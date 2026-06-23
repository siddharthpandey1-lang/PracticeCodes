print("are the functions working?")
User_input = input("yes or no: ")
if User_input.lower() == "yes":
    print("Great! Let's continue.")
else:
    print("No worries! Let's troubleshoot the functions together.")
print("Please enter a number to test the function:")
if User_input.isdigit():
    number = int(User_input)
    result = number * 2  # Example function: doubling the input
    print("The result of doubling {number} is {result}.")
print("Thank you for testing the functions!")


