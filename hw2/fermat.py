def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print 'Holy Smokes, Fermat was wrong!'
	elif n <= 2:
		print "No, that doesn't work"

def user_fermat():
	a = int(raw_input('A = '))
	b = int(raw_input('B = '))
	c = int(raw_input('C = '))
	n = int(raw_input('N = '))
	check_fermat(a, b, c, n)
