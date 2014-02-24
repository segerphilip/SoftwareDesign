"""
Program: snow_flake_side
Author: Philip Seger
Date: 2/18/14
"""

def snow_flake_side(turtle,l,level):
    #begin by drawing equilateral triangle
    if level == 1:
        fd(turtle,l)
        rt(turtle,60)
        fd(turtle,l)
        lt(turtle,120)
        fd(turtle,l)
        rt(turtle,60)
    else:
        snow_flake_side(turtle,l/3,level-1)
        turtle.rt(60)
        snow_flake_side(turtle,l/3,level-1)
        turtle.lt(120)
        snow_flake_side(turtle,l/3,level-1)
        turtle.rt(60)
        snow_flake_side(turtle,l/3,level-1)
        turtle.undraw()

if __name__=='__main__':
    from swampy.TurtleWorld import *    
    world = TurtleWorld()
    alice = Turtle()
    alice.delay=0.01
    snow_flake_side(alice,50,3)
    wait_for_user()
