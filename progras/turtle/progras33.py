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
        self.color = choice(colors) # случайный цвет из списка
  
    def paint(self, r, c):
        x1 = x0 + c * m + d
        # рассчитать координаты левого верхнего угла.
        y1 = y0 + r * m + d
        # координаты правого нижнего угла.
        x2 = x1 + m - 2*d # - r
        y2 = y1 + m - 2*d
        self.id = canv.create_rectangle(x1,y1,x2,y2,fill = self.color) # квадратик ячейки
        # текст в центр ячейки
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        self.id_text = canv.create_text(x,y, text = self.n, font = "Arial " + str(m//2)) # текст в квадратике, размер зависит от масштаба
  
a = []
for r in range(nr): # 6 строк
    a.append([]) # создаем пустую строку
    for c in range(nc): # в каждой строке - 10 элементов
        a[r].append(cell(r,c)) # добавляем очередной элемент в строку
         
def paint(): # функция для отрисовки всего списка
    canv.delete(ALL)
    for r in range(nr):
        for c in range(nc):
            a[r].paint(r,c) # поскольку ячейка не знает, где она находится, надо сказать ей, чтобы она могла себя нарисовать
 
def fill_random(event = 0):
    for r in range(nr):
        for c in range(nc):
            a[r].n = rnd(10)
    paint()
 
 
def task(event):
    pass
     
fill_random()
     
canv.bind('<3>', task)   
canv.bind('<1>', fill_random)   
 
mainloop()