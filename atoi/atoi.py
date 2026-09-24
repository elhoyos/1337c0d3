# uv run atoi.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import re

def myAtoi(s):
	"""
	Intuition: follow the given algorithm in an ordered fashion.
	1. regexp match digits
	2. convert based on each number's place value (units, tens, hundreds, etc.)
	3. keep within bounds
	"""
	ASCII_0 = ord("0")
	MAX_INT = (2 ** 31) - 1
	MIN_INT = -2 ** 31

	match = re.match(r'^ *(\-|\+)?0*([0-9]+)', s)
	if match == None:
		return 0

	sign = match.group(1) if match.group(1) else "+"
	digits = match.group(2)

	# conversion
	integer = 0
	n_digits = len(digits)
	# print("n_digits=%s" % n_digits)
	for i in range(n_digits):
		digit = digits[i]
		d_int = ord(digit) - ASCII_0
		place_value = 10 ** (n_digits - 1 - i)
		integer += d_int * place_value
		# print("i=%s, d_int=%s, place_value=%s, integer=%s" % (i, d_int, place_value, integer))

	if sign == "-":
		integer = -integer

	if integer > MAX_INT:
		return MAX_INT

	if integer < MIN_INT:
		return MIN_INT

	return integer

def test():
    tests = [
        [
			"42",
			42
		],
		[
			"   -042",
			-42
		],
		[
			"1337c0d3",
			1337
		],
		[
			"0-1",
			0
		],
		[
			"words and 987",
			0
		],
    ]

    for input, want in tests:
        res = myAtoi(input)
        if want != res:
            raise RuntimeError(f"Unexpected response, want={want}, got={res}")


if __name__ == "__main__":
    test()