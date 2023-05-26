from tkinter import *
from random import *
import time

class Ball:
    def __init__(self,canvas,color,winW,winH,racket):
        self.canvas=canvas
        self.racket=racket
        self.id=canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.id,winW/2,winH/2)
        startpos=[-3,-2,-1,1,2,3]
        shuffle(startpos)
        self.x=startpos[0]
        self.y=-step
        self.nottouchbottom=True
        
    def ballmove(self):
        self.canvas.move(self.id,self.x,self.y)
        ballPos=self.canvas.coords(self.id)
        if ballPos[1]<=0:
            self.y=step
        if ballPos[2]>=winW:
            self.x=-step
        if ballPos[3]>=winH:
            self.y=-step
        if ballPos[0]<=0:
            self.x=step
        if self.hitracket(ballPos)==True:
            self.y=-step
        if ballPos[3]>=winH:
            self.nottouchbottom=False
        
    
    def hitracket(self,pos):
        racketPos=self.canvas.coords(self.racket.id)
        if pos[2]>=racketPos[0] and pos[0]<=racketPos[2]:
            if pos[3]>=racketPos[1] and pos[3]<=racketPos[3]:
                return True
        return False
        
class Racket:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,winW/2,400)
        self.x=0
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    
    def turn_left(self,event):
        self.x=-3
    def turn_right(self,event):
        self.x=3
    def racketmove(self):
        self.canvas.move(self.id,self.x,0)
        racketPos=self.canvas.coords(self.id)
        if racketPos[0]<=0:
            self.x=0
        if racketPos[2]>=winW:
            self.x=0
        
step=3
winW=640
winH=480
speed=0.03

tk=Tk()
tk.title("Bounce")
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=winW,height=winH,
              bd=0,highlightthickness=0)
canvas.pack()
tk.update()

racket=Racket(canvas,'blue')
ball = Ball(canvas,'red',winW,winH,racket)


while ball.nottouchbottom:
    try:
        ball.ballmove()
    except:
        print("Game Over")
        break
    racket.racketmove()
    tk.update_idletasks()#更新所有的idle tasks
    tk.update()#更新所有的視窗
    time.sleep(speed)