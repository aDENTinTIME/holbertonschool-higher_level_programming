#!/usr/bin/python3

def pow(a, b):
	c = a
	while b:
		c *= a
		if b > 0:
			b -= 1
		else:
			b += 1
	return c / a
