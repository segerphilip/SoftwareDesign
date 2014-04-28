def compute_binomial_coeff_recursive(n, k):
	if k > n:
		return 
	elif (n is 1 and k is 1) or (k is 0):
		return 1
	else:
		return compute_binomial_coeff_recursive(n-1, k-1) + compute_binomial_coeff_recursive(n-1, k)

if __name__ == '__main__':
	print compute_binomial_coeff_recursive(2,2)