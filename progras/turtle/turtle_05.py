from turtle import *
from random import randrange as rnd
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'black', 'gray', 'lightgreen']
speed(100)
pu()
for z in range(1000):
    color(colors[rnd(len(colors))],colors[rnd(len(colors))])
    x = rnd(-200,200)
    y = rnd(-200,300)
    setpos(x,y)
    pd()
    begin_fill()
    circle(rnd(10,50))
    end_fill()
    pu()
done()
