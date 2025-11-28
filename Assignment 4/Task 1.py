# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

reading_file = open("./Sample.txt", 'r')

line1 = reading_file.readline()
line2 = reading_file.readline()

print("Reading file content:")
print(f"Line 1 : {line1}")
print(f"Line 2 : {line2}")

reading_file.close()
