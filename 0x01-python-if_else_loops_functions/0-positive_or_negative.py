#!/usr/bin/python3
import random
number = random.randint(-10, 10)

result = ""
if number > 0:
    result = "{:d} is positive"
elif number < 0:
    result = "{:d} is negative"
else:
    result = "{:d} is zero"

print(result.format(number))
