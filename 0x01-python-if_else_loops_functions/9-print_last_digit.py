#!/usr/bin/python3

def print_last_digit(number):
	string = str(number)
	print(string[-1:], end="")
	return int(string[-1:])
