#!/usr/bin/python3
def fizzbuzz():
	output = ""
	for i in range(1, 101):
		is_divisible_by_3 = i % 3 == 0
		is_divisible_by_5 = i % 5 == 0

		if is_divisible_by_3 and is_divisible_by_5:
			output += "FizzBuzz "
		elif is_divisible_by_3:
			output += "Fizz "
		elif is_divisible_by_5:
			output += "Buzz "
		else:
			output += str(i) + " "

	print(output)
