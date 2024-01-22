#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_copie = number
l_digit = 0
if number < 0:
    number_copie *= -1
    l_digit = -1 * (number_copie % 10)
else:
    l_digit = number % 10
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
else:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
