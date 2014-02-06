def get_complementary_base(nucleotide):
	if nucleotide == 'a':
		return 't'
	elif nucleotide == 't':
		return 'a'
	elif nucleotide == 'c':
		return 'g'
	elif nucleotide == 'g':
		return 'c'
	else:
		return 'Wrong input! Error #1'
