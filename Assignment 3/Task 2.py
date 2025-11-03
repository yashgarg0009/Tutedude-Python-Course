# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
#          Square root of the number
#          Natural logarithm (log base e) of the number
#          Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
number = float(input("Enter a number: "))
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)
print(f"Square root of {number} is {square_root}")
print(f"Natural logarithm of {number} is {natural_log}")
print(f"Sine of {number} (in radians) is {sine_value}")
