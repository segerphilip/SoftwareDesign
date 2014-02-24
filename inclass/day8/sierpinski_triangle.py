"""
Program: sierpinski_triangle
Author: Philip Seger
Date: 2/18/14
"""

def sierpinski_triangle_a(turtle,length,level):
   fd(turtle,length)
   lt(turtle,120)
   fd(turtle,length)
   lt(turtle,120)
   fd(turtle,length)
   if level == 0:
    	return 
    clone_of_turtle = Turtle()
    clone_of_turtle.x = turtle.x
    clone_of_turtle.y = turtle.y
    clone_of_turtle.heading = turtle.heading
    sierpinski_triangle_b(clone_of_turtle,branch_length/2,level-1)
    clone_of_turtle.undraw()

def sierpinski_triangle_b(turtle,length,level):




if __name__=='__main__':
    from swampy.TurtleWorld import *    
    world = TurtleWorld()
    alice = Turtle()
    alice.delay=0.01
    sierpinski_triangle_a(alice,50,3)
    sierpinski_triangle_b(alice,50,3)
    wait_for_user()
