def sum_numbers_not_divisible_by_four(n):
	total = 0
	if n == 0:
		return total
	elif n % 4 == 0:
		return sum_numbers_not_divisible_by_four(n - 1)
	else:
		total += n
		return total + sum_numbers_not_divisible_by_four(n - 1)

if __name__ == '__main__':
	print sum_numbers_not_divisible_by_four(8)