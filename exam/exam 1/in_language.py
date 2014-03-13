def in_language(word):
	countera = 0
	counterb = 0
	i = 0
	while i < len(word):
		if word[i:i+1] == 'a':
			countera += 1
		elif word[i:i+1] == 'b':
			counterb += 1
		i += 1
	if counterb != countera:
		return False
	else:
		return True

print in_language('aaaabbbb')