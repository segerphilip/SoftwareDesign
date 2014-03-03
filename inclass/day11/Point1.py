"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""
import math

class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(p1,p2):
    distance = math.sqrt((p1.x + p2.x)**2 + (p1.y + p2.y)**2)
    print distance

class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def main():
    blank = Point()
    blank.x = 3
    blank.y = 4

    blank1 = Point()
    blank1.x = 5
    blank1.y = 2

    distance_between_points(blank,blank1)
    print 'blank',
    print_point(blank)
    
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height

    box1 = Rectangle()
    box.width = 50.0
    box.height = 20.0
    box.corner = Point()
    box.corner.x = 2.0
    box.corner.y = 3.0
    move_rectangle(box1, 6, 4)

if __name__ == '__main__':
    main()

