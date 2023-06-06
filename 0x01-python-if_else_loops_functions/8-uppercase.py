#!/usr/bin/python3
def uppercase(str):
	converted_str = ""
	for char in str:
		if "a" <= char <= "z":
			converted_str += chr(ord(char) - 32)
		else:
			converted_str += char
	print(converted_str)
