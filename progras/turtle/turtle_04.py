from turtle import *
color('orange')
width(3)
speed(0)

def mn(n):
    for z in range(n):
        fd(200/n)
        rt(360/n)

n = 8

for z in range(1,7000,5):
    fd(20)
    rt(z)
ht()

done()

