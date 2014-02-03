#+ - - - - + - - - - +
#|		  |			|
#|		  |			|
#|		  |			|
#|		  |			|
#+ - - - - + - - - - +
#|		  |			|
#|		  |			|
#|		  |			|
#|		  |			|
#+ - - - - + - - - - +
def small_grid():
	line = '+ - - - - + - - - - +\n'
	sides = '|	  |	    |\n'
	print line, 4 * sides, line, 4 * sides, line

def big_grid():
	line = '+ - - - - + - - - - + - - - - + - - - - +\n'
	sides = '|	  |	    |	      |	        |\n'
	print line, 4 * sides, line, 4 * sides, line, 4 * sides, line, 4 * sides, line

