#!/usr/bin/python3

for digit1 in range(9):
    start_digit2 = digit1 + 1
    end_digit2 = 10 if digit1 == 8 else 10 - digit1 - 1

    for digit2 in range(start_digit2, end_digit2):
        print("{:d}{:d}".format(digit1, digit2), end=", ")

print("89")
