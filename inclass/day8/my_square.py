"""
Program: my_square
Author: Philip Seger
Date: 2/18/14
"""

def my_square(turtle,side_length, starting_x, starting_y):
    #set a starting x position
    turtle.x = starting_x
    #set a starting y position
    turtle.y = starting_y
    #start drawing the square
    fd(turtle,side_length)
    lt(turtle,90)
    fd(turtle,side_length)
    lt(turtle,90)
    fd(turtle,side_length)
    lt(turtle,90)
    fd(turtle,side_length)
    #ending spin animation
    lt(turtle,90)
    rt(turtle,90)

if __name__=='__main__':
    from swampy.TurtleWorld import *    
    world = TurtleWorld()
    alice = Turtle()
    my_square(alice,30, 15, 15)
    wait_for_user()
