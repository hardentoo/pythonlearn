from tkinter import *
root = Tk()
root.geometry('800x600+550+200')

canv = Canvas(root,bg='white') # создать в окне root, фон - белый
canv.pack(fill=BOTH,expand=1) # размер - максимально возможный в обе стороны

canv.create_rectangle(30,50,120,80,fill='green')
canv.create_line(10,100,150,10,fill='blue',width=5)
canv.create_rectangle(200,200,500,500)
canv.create_oval(200,200,500,500)
canv.create_text(350,350,text='Hello!')

for x in range(40,600,20):
    canv.create_line(x,40,x,580,fill='lightgray')
    canv.create_text(x,20,text=x,font = 'Arial 8')
     
for y in range(40,600,20):
    canv.create_line(40,y,580,y,fill='lightgray')
    canv.create_text(20,y,text=y,font = 'Arial 8')
canv.create_line(40,40,580,40,width=2,arrow='last')
canv.create_line(40,40,40,580,width=2,arrow='last')

mainloop()
