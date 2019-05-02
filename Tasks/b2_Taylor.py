"""
Taylor series
"""
import math

def ex(x) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	value = 1
	for i in range(1, 10):
		value += x ** i / math.factorial(i)
	return value


def sinx(x) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	value = x
	for i in range(1, 10):
		value += ((-1)** i) * ( x ** (2 * i + 1) / math.factorial(2 * i + 1))
	return value

print(sinx(0))