from turtle import *
from random import randrange as rnd
 
speed(0)
 
def sq(a):
    rt(rnd(360))
    color('green','lightgreen')
    begin_fill()
    pd()
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    pu()
    end_fill()
 
sq(90)
done()
