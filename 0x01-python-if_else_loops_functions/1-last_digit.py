#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ten = -10
else:
    ten = 10
last_digit = number % ten
if last_digit > 5:
    string = " and is greater than 5"
elif last_digit == 0:
    string = " and is 0"
elif last_digit < 5:
    string = " and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit}" + string)