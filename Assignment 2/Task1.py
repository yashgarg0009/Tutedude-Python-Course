# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

num = int(input("Enter a number : "))

if num % 2 == 0 :
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")