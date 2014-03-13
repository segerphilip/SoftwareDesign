def sum_squares_even(n):
	if n % 2 != 0:
		n = n - 1
	if n == 0:
		return n
	else:
		return n ** 2 + sum_squares_even(n-2)

print sum_squares_even(5)