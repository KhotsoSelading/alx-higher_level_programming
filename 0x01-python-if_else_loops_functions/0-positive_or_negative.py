#!/usr/bin/python3
import random
number = random.randint(-10, 10)

output = "{:d} is ".format(number)

if number > 0:
	output += "positive"
elif number == 0:
	output += "zero"
else:
	output += "negative"

print(output)
