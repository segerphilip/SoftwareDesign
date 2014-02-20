# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
@coauthor: segerphilip
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import *

def build_random_function(min_depth, max_depth):
    """ Takes min_depth and max_depth to then create a random list
        which is later used.

        returns a random list []
    """
    #new list needed as a throwaway base condition
    new_list = [["x"], ["y"]]
    #base condition if max_depth is 1, return 
    if max_depth == 1:
        return new_list[randint(0,1)]

    #defining a and b depending on min and max depth - 1 for proper index
    a = build_random_function(min_depth - 1, max_depth - 1)
    b = build_random_function(min_depth - 1, max_depth - 1)

    #all the functions that can be used
    function_list = [["prod", a, b], ["cos_pi", a], ["sin_pi", a], ["squared", a], ["cubed", b], ["x"], ["y"]]

    #if min_depth is greater or equal to 0, it can pick from the first 4 functions
    if min_depth >= 0:
        return function_list[(randint(0,4))]
    #if min_depth is less, it can use all 6
    elif min_depth < 0:
        return function_list[(randint(0,6))]


def evaluate_random_function(f, x, y):
    """ Takes the random function built by build_random_function, along
        with x and y as points of evaluation

        returns the mathematical values of the random function
    """
    #evaluate for product
    if f[0] == "prod":
        return evaluate_random_function(f[1],x,y) * evaluate_random_function(f[2],x,y)
    #evaluate for cos pi
    elif f[0] == "cos_pi":
        return cos(pi * evaluate_random_function(f[1],x,y))
    #evaluate for sin pi
    elif f[0] == "sin_pi":
        return sin(pi * evaluate_random_function(f[1],x,y))
    #evaluate for square
    elif f[0] == "squared":
        return evaluate_random_function(f[1],x,y) ** 2
    #evaluate for cubed
    elif f[0] == "cubed":
        return evaluate_random_function(f[1],x,y) ** 3
    #evaluate for x
    elif f[0] == "x":
        return x
    #evaluate for y
    elif f[0] == "y":
        return y

#def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
#    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
#        to the output interval [output_interval_start, output_interval_end].  The mapping
#        is an affine one (i.e. output = input*c + b).
#    
#        TODO: please fill out the rest of this docstring
#    """
#    # your code goes here

def draw_function():
    """ Don't want to use remap_interval, too many inputs and not
        fully needed. Instead, draw_function used without any input
        that draws the function from build_random_function.

        Saves a .png picture in the base folder.
    """

    #define some bounds for the random function
    red = build_random_function(1,8)
    green = build_random_function(4,6)
    blue = build_random_function(5,7)

    #used to initialize the image and save pixels properly
    im = Image.new("RGB",(350,350))
    pixels = im.load()

    #run through the x and y pixels from 0 to 349 and color them
    for x in range(0,349):
        for y in range(0,349):
            #define the scale from -1 to 1
            xscale = x / (349 / 2.0) - 1
            yscale = y / (349 / 2.0) - 1
            #call evaluate_random_function with the color, x and y scale
            r = evaluate_random_function(red,xscale,yscale)
            g = evaluate_random_function(green,xscale,yscale)
            b = evaluate_random_function(blue,xscale,yscale)
            #rescale everything back up correctly so it can be added to the picture
            r_rescaled = (r + 1) * 255 / 2.0
            g_rescaled = (g + 1) * 255 / 2.0
            b_rescaled = (b + 1) * 255 / 2.0
            #from floating point/double to int so it fits the grid correctly
            r = int(r_rescaled)
            g = int(g_rescaled)
            b = int(b_rescaled)
            #plot
            pixels[x,y] = (r,g,b)
    #save the image and show it
    im.save("pic1.png")
    im.show()