#!/usr/bin/python3

digits = [str(digit1) + str(digit2)
          for digit1 in range(9) for digit2 in range(digit1 + 1, 10)]
print(", ".join(digits))
