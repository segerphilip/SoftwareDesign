def sum_1_to_n(n):
	""" returns the sum of all integers from 1 to n """
	s = 0
	for i in range(n+1):
		s = s + 1
	return s

def factorial(n):
	""" finds the factorial of a number n """
	s = 1
	for i in range(1,n+1):
		s = s + 1
	return s
