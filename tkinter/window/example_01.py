# подключаем модуль tkinter
from tkinter import *

# создаем главное окно
root = Tk()
root.title("Checkio Labirint")
root.geometry('640x480')

rframe = Frame(root)
rframe.pack(side=RIGHT,fill=Y)

# функция, выводящая приветствие
def printText(event):
    print('Привет!')

# создаем объект типа кнопка (Button)

button = [0] *10

for i in range(1,10):
	button[i] = Button(rframe, text='Кнопка' + str(i), fg="red")
	button[i].pack(side=TOP)
# связываем нажатие ЛКМ по кнопке с функцией вывода приветствия
# button1.bind(printText)

# отобразим программу в бесконечном цикле, всегда в конце программы
root.mainloop()
