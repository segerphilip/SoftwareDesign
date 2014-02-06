from random import random
def random_float(start, stop):
	""" takes a base and returns the corresponding complement """
	return (start + (random.random() * stop - random.random() * start))
