#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 bsd <hardenedgentoo@gmail.com>
#
# Distributed under terms of the MIT license.


import time
from tkinter import *

root = Tk()

w, h = (800, 800)
n, m = (40, 40)
dw, dh = (w/n, h/m)

a = [[0 for x in range(m)] for y in range(n)]
b = [[0 for x in range(m)] for y in range(n)]

root.geometry('800x800+550+100')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)


def cell_add(event):
    i = int(event.x // dw)
    j = int(event.y // dh)
    a[i][j] = 1
    canvas_update()


def cell_del(event):
    i = int(event.x // dw)
    j = int(event.y // dh)
    a[i][j] = 0
    canvas_update()


def log (a):
    for i in range (0, len(a)-1):
        print(a[i])


def canvas_update():

    canv.delete(ALL)

    for x in range(1, n):
        canv.create_line(x*dw,0,x*dw,h,fill='lightgray')

    for y in range(1, m):
        canv.create_line(0,y*dh,w,y*dh,fill='lightgray')

    for x in range(1, n):
        for y in range(1, m):
            if (a[x][y] == 1):
                canv.create_rectangle(dw*x,dh*y,dw+dw*x,dh+dh*y,fill='orange')


def life_run(event):
    for l in range(1,100):
        for i in range (2, n-1):
            for j in range (2, m-1):
                count = 0
                count += a[i-1][j-1] + a[i-1][j] + a[i-1][j+1]
                count += a[i][j-1]   + a[i][j]   + a[i][j+1]
                count += a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]

                if (count == 3):
                    b[i][j] = 1
                else:
                    b[i][j] = 0

        flag = 0
        for i in range (1, n):
            for j in range(1, m):
                a[i][j] = b[i][j]
                flag += a[i][j]

        canvas_update()
        root.update()
        time.sleep(0.2)
        if (flag == 0):
            break


def key(event):
    if (event.char == 'q'):
        canv.delete(ALL)
        root.destroy()

canv.bind('<B1-Motion>', cell_add)
canv.bind('<B3-Motion>', cell_del)
canv.bind('<Button-1>', cell_add)
canv.bind('<Button-3>', cell_del)
canv.bind('<Button-2>', life_run)
root.bind("<Key>", key)

canvas_update()
mainloop()
