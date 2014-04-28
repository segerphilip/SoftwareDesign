import numpy

def count_frequencies_of_first_letters(L):
	d = dict()
	for n in range(len(L)):
		h = histogram(L(n:n+1))
		for m in h:
			d[m] += h

if __name__ == '__main__':
	L = ['apples' , 'pair', 'pear', 'banana']
	print count_frequencies_of_first_letters(L)