"""
Program: exclusive_or_dict
Author: Philip Seger
Date: 3/6/14
"""

def exclusive_or_dict(di, d2):
    #print d1
    #print d2
    counter = 0
    d3 = dict()
    for c in d1:
        if not c in d2:
            d3[c] = d1[c]

    for d in d2:
        if not d in d1:
            d3[d] = d2[d]

    print d3

if __name__=='__main__':
    d1 = {'a':5, 'b':3}
    d2 = {'a':7, 'c':3}
    exclusive_or_dict(d1, d2)
