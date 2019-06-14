from turtle import *
from random import *

def randomcolor():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    color(r,g,b)

def randomplace():
    x=randint(-300,300)
    y=randint(-300,300)
    penup()
    goto(x,y)
    pendown()

def randomheading():
    h=randint(0,359)
    setheading(h)

def randomshape():
    shapes=["turtle","arrow","circle","square","triangle","classic"]
    s=randint(0,5)
    shape(shapes[s])

colormode(255)
shape("turtle")

for i in range(300):

    randomcolor()
    randomplace()
    randomheading()
    randomshape()
    stamp()
