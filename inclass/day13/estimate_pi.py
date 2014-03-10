import math

def estimate_pi():
	k = 0
	value = 0.0
	while k < 5:
		value = (math.factorial(4.0 * k) * (1103.0 + 26390.0 * k)) / (math.factorial(k)**4 * 396**(4 * k))
	value *= ((2.0 * 2.0**(-1.0/2.0)) / 9801.0)
	return value

print estimate_pi()