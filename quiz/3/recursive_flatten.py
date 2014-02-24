def recursive_flatten(some_list):
	flat_list = []
	for i in some_list:
		if type(i) == list:
			flat_list.extend(recursive_flatten(i))
		else:
			flat_list.append(i)
	return flat_list

if __name__=='__main__':
	some_list = [1, 2, [3, 5]]
	recursive_flatten(some_list)
