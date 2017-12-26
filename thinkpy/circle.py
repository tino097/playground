from math import pi
from swampy.TurtleWorld import *


def circle(t, r):
    circumference = 2 * pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

world = TurtleWorld()
bob = Turtle()

circle(bob, 30)
