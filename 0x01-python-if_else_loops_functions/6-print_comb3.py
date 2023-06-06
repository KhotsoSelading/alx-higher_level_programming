#!/usr/bin/python3

for number in range(10, 100):
    tens_digit = number // 10
    ones_digit = number % 10

    if tens_digit < ones_digit:
        print("{:02d}".format(number), end=', ')

print("89")
