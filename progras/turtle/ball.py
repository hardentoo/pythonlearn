from tkinter import *
from random import randrange as rnd, choice
 
root = Tk()
root.geometry('600x600+100+100')
canv = Canvas(bg='white')
canv.pack(fill=BOTH,expand=1)
 
 
vx = 2
vy = 1
r = 10
x = 300
y = 300
canv.create_rectangle(50-r,50-r,550+r,550+r)
def update():
    global x,y,vx,vy
    x += vx
    y += vy
    if x > 550:
        vx *= -1        
        x = 550 # чтобы изображение мяча не выходилао за рамку
    if x < 50:
        vx *= -1
        x = 50 # чтобы изображение мяча не выходилао за рамку
         
    if y > 550:
        vy *= -0.6        
        y = 550
        vx *= 0.6
    vy += 1
         
    canv.delete('ball')
    canv.create_oval(x-r,y-r,x+r,y+r,fill='orange', tag = 'ball')
     
    root.after(30,update)
 
def click(event):
    global vy,vx
    dx = event.x - x
    dy = event.y - y
    if dx != 0 and dy != 0:
        vx = 20*(dx/abs(dx))
        vy = 20*(dy/abs(dy))
     
 
canv.bind('<1>',click)
 
update()
root.mainloop()
