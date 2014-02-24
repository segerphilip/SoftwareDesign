"""
Program: my_triangle
Author: Philip Seger
Date: 2/18/14
"""

def my_triangle(turtle,side_length):
    fd(turtle,side_length)
    lt(turtle,120)
    fd(turtle,side_length)
    lt(turtle,120)
    fd(turtle,side_length)

if __name__=='__main__':
    from swampy.TurtleWorld import *    
    world = TurtleWorld()
    alice = Turtle()
    my_triangle(alice,30)
    wait_for_user()
