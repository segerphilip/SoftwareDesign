def pair_list_to_dictionary(words):
	d1 = dict()
	i = 0
	if len(words) % 2 != 0:
		words = words[0:len(words)-1]
	while i < len(words):
		d1[words[i]] = words[i+1]
		i += 2
	return d1

print pair_list_to_dictionary(['hello','a','test','b'])