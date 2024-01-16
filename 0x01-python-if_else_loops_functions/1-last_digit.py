#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")
if number < 0:
    num = abs(number) % 10 * -1
else:
    num = abs(number) % 10
if num > 5:
    print(f"{num} and is greater than 5")
elif num < 5 and number != 0:
    print(f"{num} and is less than 6")
else:
    print(f"{num} and is 0")
