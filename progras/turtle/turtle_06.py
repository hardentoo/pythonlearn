from turtle import *
from random import randrange as rnd
colors = ['red','orange','yellow','green','cyan','blue','magenta','black','gray','lightgreen']
speed(100)
 
def star(z,n):
    a = 360/n
    for d in range(n):
        fd(z)
        rt(180-a)
 
up()
for z in range(120):
    color(colors[rnd(len(colors))],colors[rnd(len(colors))])
    x = rnd(-200,200)
    y = rnd(-200,300)
    goto(x,y)
    down()
    begin_fill()
    star(50,rnd(1,30))
    end_fill()
    up()
done()
