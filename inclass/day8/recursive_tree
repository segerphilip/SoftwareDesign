"""
Program: recursive_tree
Author: Philip Seger
Date: 2/18/14
"""

def recursive_tree(turtle,branch_length,level):
    fd(turtle,branch_length)
    if level == 0:
    	return
    clone_of_turtle = Turtle()
    clone_of_turtle.x = turtle.x
    clone_of_turtle.y = turtle.y
    clone_of_turtle.heading = turtle.heading
    lt(clone_of_turtle,30)
    recursive_tree(clone_of_turtle,branch_length*.6,level-1)
    clone_of_turtle.undraw()
    clone_of_turtle.x = turtle.x
    clone_of_turtle.y = turtle.y
    clone_of_turtle.heading = turtle.heading
    rt(clone_of_turtle,40)
    recursive_tree(clone_of_turtle,branch_length*.8,level-1)
    clone_of_turtle.undraw()
    turtle.undraw()

if __name__=='__main__':
    from swampy.TurtleWorld import *    
    world = TurtleWorld()
    alice = Turtle()
    alice.delay=0.01
    recursive_tree(alice,100,10)
    wait_for_user()