
from turtle import *
from random import randrange as rnd

color('red','yellow')
speed(10)
pu()

for z in range(12):
    x = rnd(-200,200)
    y = rnd(-200,300)
    setpos(x,y)
    pd()
    begin_fill()
    circle(rnd(10,50))
    end_fill()
    pu()

done()
