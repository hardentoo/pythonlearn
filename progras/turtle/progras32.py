from random import randrange as rnd, choice
from tkinter import *
import itertools
  
root = Tk()
root.geometry('800x600')
  
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
 
 
m = 34 # размер ячеек
d = 2 # размер поля вокруг ячейки
nr = 6 # количество строк
nc = 8 # количество столбцов
x0 = m // 2 # отступ от левого края
y0 = m // 2 # отступ от вернего края
colors = ['red','yellow','cyan','green']
  
class cell():
    def __init__(self, r, c): # при создании указываем номер строки и столбца, в который помещаем
        self.n = rnd(10) # значение, с которым будем работать
        self.r = r # Номер сторки в двумерном списке.
        self.c = c # Номер столбца ...
        self.color = choice(colors) # случайный цвет из списка
        self.id = canv.create_rectangle(-100,0,-100,0,fill = self.color) # квадратик ячейки
        self.id_text = canv.create_text(-100,0, text = self.n, font = "Arial " + str(m//2)) # текст в квадратике, размер зависит от масштаба
        self.paint()
  
    def paint(self):
        x1 = x0 + self.c * m + d
        # рассчитать координаты левого верхнего угла.
        y1 = y0 + self.r * m + d
        # координаты правого нижнего угла.
        x2 = x1 + m - 2*d # - r
        y2 = y1 + m - 2*d
        canv.coords(self.id,x1,y1,x2,y2)
        canv.itemconfig(self.id,fill = self.color)
        # текст в центр ячейки
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        canv.coords(self.id_text,x,y)
        canv.itemconfig(self.id_text, text = self.n)
  
a = []
for r in range(nr): # 6 строк
    a.append([]) # создаем пустую строку
    for c in range(nc): # в каждой строке - 10 элементов
        a[r].append(cell(r,c)) # добавляем очередной элемент в строку


def mark(rr,cc):
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        r = dr + rr
        c = dc + cc
        if r in range(nr) and c in range(nc):
            a[r].color = 'orange'
            a[r].paint()

 
def task(event):
    for r in range(nr):
        for c in range(nc):
            a[r].color = 'gray'
            a[r].paint()
    rr = (event.y - y0) // m
    cc = (event.x - x0) // m
    for dr,dc in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
        r = dr + rr
        c = dc + cc
        if r in range(nr) and c in range(nc):
            mark(r,c)

canv.bind('<3>', task)   
mainloop()