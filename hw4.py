#Assignment 4
#David Parrott
#27 September, 2011
from turtle import *
from random import *
"""this first function recursively draws a spiral of length, initialLength/
turning at angle, turnAngle, and decreasing in size by, multiplier with/
each turn"""
def spiral(initialLength, turnAngle, multiplier):
    hideturtle()
    colormode(255)
    R=choice(range(255))
    G=choice(range(255))
    B=choice(range(255))
    pencolor(R,G,B)    
    if initialLength<=1.0:
        done()
    else:
        forward(initialLength)
        left(turnAngle)
        return spiral(initialLength*multiplier, turnAngle, multiplier)

"""this function recursively draws a branching structure 'levels'/
deep. each branch is half the trunkLength"""
def svTree(trunkLength,levels):
    hideturtle()
    colormode(255)
    R=choice(range(255))
    G=choice(range(255))
    B=choice(range(255))
    pencolor(R,G,B)
    forward(trunkLength)
    right(30)
    forward(trunkLength/2)
    if levels>0:
        svTree(trunkLength/2,levels-1)
    back(trunkLength/2)
    left(60)
    forward(trunkLength/2)
    if levels>0:
        svTree(trunkLength/2, levels-1)
    back(trunkLength/2)
    right(30)
    back(trunkLength)

"""this function sets up a Koch Snowflake with 'levels' number of facets/
along a triangle 'lengthSide' long,which sets up the triangular framework while/
'snowside' handles the recursion on each side"""
def snowflake(lengthside, levels):
    hideturtle()
    for side in range(3):
        snowside(lengthside, levels)
        right(120)
    
def snowside(lengthSide, levels):
    hideturtle()
    colormode(255)
    R=choice(range(255))
    G=choice(range(255))
    B=choice(range(255))
    pencolor(R,G,B)
    if levels == 0:
        forward(lengthSide)
        returndone()
    snowside(lengthSide, levels-1)
    left(60)
    snowside(lengthSide, levels-1)
    right(120)
    snowside(lengthSide, levels-1)
    left(60)
    snowside(lengthSide, levels-1)

