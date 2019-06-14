from turtle import *
from random import randint

colormode(255)
rl=255
gl=255
bl=0
rf=randint(0,255)
gf=randint(0,255)
bf=randint(0,255)

shape("turtle")
pensize(10)

begin_fill()
while True:
    forward(300)
    left(150)
    rl = randint(0,255)
    gl = randint(0,255)
    bl = randint(0,255)
    color((rl,gl,bl),(rf,gf,bf))
    if abs(pos()) < 1:
        break
end_fill()
done()


