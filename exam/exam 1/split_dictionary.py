def split_dictionary(d1):
	uppercase = dict()
	lowercase = dict()
	for i in d1:
		if i == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
			uppercase[i] = d1[i]
		else:
			lowercase[i] = d1[i]
	return uppercase, lowercase


print split_dictionary({'a':2,'B':'hello','c':'t'})