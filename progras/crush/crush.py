from tkinter import *
from random import randrange as rnd
import time
from PIL import Image, ImageTk



class crush():
    def __init__(self,geometry=363,indent=15,numbers=15,fluctuation=100):
        self.root = Tk()
        scale = str(str(geometry+2*indent)+'x'+str(geometry+2*indent))
        self.root.geometry(scale)
        self.canv = Canvas(bg='white')
        self.but = Button(self.root,bg='white',borderwidth=0,highlightcolor='white',width=363, text = "To start click any square")
        self.but.pack()
        self.canv.pack(fill = BOTH, expand = 1)
        self.canv.bind('<Button>',self.start)

        self.numbers = numbers
        self.fluctuation = fluctuation

        self.indent = indent
        self.period = 26
        self.numbers = numbers
        self.score = 0

        self.radius = self.period//2

        self.colors = [ImageTk.PhotoImage(file="red.png"),
                       ImageTk.PhotoImage(file="blue.png"),
                       ImageTk.PhotoImage(file="green.png"),
                       ImageTk.PhotoImage(file="yellow.png"),
                       ImageTk.PhotoImage(file="cyan.png")]
        self.orange = ImageTk.PhotoImage(file="oranger.png")



        self.field = [[rnd(3)+1 for c in range(self.numbers)]for r in range(self.numbers)]
        self.field_print()


    def oranger(self,r,c):
        y = r*self.period + self.indent
        x = c*self.period + self.indent
        self.canv.create_image(x, y, image=self.orange)
        self.canv.update()

    def delete(self):
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c]:
                    for i in range(r,0,-1):
                        self.field[i][c] = self.field[i-1][c]
                        self.map[i][c] = self.map[i-1][c]
                    
                    self.field[0][c] = 0
                    self.map[0][c] = 0
        

        for c in range(len(self.field[0])-1,-1,-1):
            s = 0
            for r in range(len(self.field)):
                s += self.field[r][c]
            if not s:
                if c < len(self.field[0])-1:
                    for r in range(len(self.field)):
                        self.field[r][c] = self.field[r][c+1]
                        self.map[r][c] = self.map[r][c+1]
                        
                        self.field[r].pop()
                        self.map[r].pop()

        self.field_print()






    
    def field_print(self):
        self.canv.delete(ALL)   
        for r in range(len(self.field)):
            for c in range(len(self.field[r])):
                y = r*self.period + self.indent
                x = c*self.period + self.indent
                rr = self.radius - 2
                if self.field[r][c]:
                    self.canv.create_image(x, y, image=self.colors[self.field[r][c]])
                else:
                    self.canv.create_rectangle(x-rr,y-rr,x+rr,y+rr,fill='white',width=0)

        self.canv.update()
        

    def play(self,now_r,now_c):
        now_r = now_r
        now_c = now_c
        self.oranger(now_r,now_c)
        self.map[now_r][now_c]+=1
        steps = 1
        for r in range(now_r-1,now_r+2):
            for c in range(now_c-1,now_c+2):
                if ((r == now_r and c != now_c) or (r != now_r  and c == now_c)) and r in range(len(self.field)) and c in range(len(self.field[0])) and self.map[r][c] < 5 and self.field[r][c] == self.field[now_r][now_c]:
                    steps += self.play(r,c)
        return steps


    def start(self,event):
        c = (event.x+self.period//2-self.indent)//self.period
        r = (event.y+self.period//2-self.indent)//self.period

        self.map = [[0 for c in range(self.numbers)]for r in range(self.numbers)]
        
        if self.field[r][c]:
            steps = self.play(r,c)
            if steps > 1:
                self.score += steps//5
                self.but.configure(text='Your score is '+str(self.score)+' points!')
                time.sleep(0.5)
                self.delete()
            else:
                self.field_print()


            


game = crush()
game.root.mainloop()