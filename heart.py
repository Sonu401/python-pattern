import turtle
from turtle import*

wn = Screen()
wn.bgcolor('black')

sonu = turtle.Turtle()
sonu.pencolor('white')

def curve():
    for i in range(200):
      sonu.rt(1)
      sonu.fd(1)
    
def heart():
    sonu.fillcolor('red')
    sonu.begin_fill()
    sonu.lt(140)
    sonu.fd(113)
    curve()
    sonu.lt(120)
    curve()
    sonu.fd(112)
    sonu.end_fill()
    
heart()
sonu.ht()

def write(message,pos):
    x,y=pos
    sonu.penup()
    sonu.goto(x,y)
    sonu.color('white')
    style=('Stenil Std', 18 ,'italic')
    sonu.write(message,font=style)
    
write('I',(-68,95))
write('L',(-55,95))
write('O',(-42,95))
write('V',(-30,95))
write('E',(-14,95))
write('Y',(10,95))
write('O',(26,95))
write('U',(45,95))

wn.mainloop()

    

    
