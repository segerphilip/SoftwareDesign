def split_dictionary(d1):
	uppercase = dict()
	lowercase = dict()
	for i in d1:
		if i.isupper() == True:
			uppercase[i] = d1[i]
		else:
			lowercase[i] = d1[i]
	return uppercase, lowercase


print split_dictionary({'a':2,'B':'hello','c':'t', 'D':'cake'})