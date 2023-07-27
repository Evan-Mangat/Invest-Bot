def randomColor(): 
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    returnedcolor = (r,g,b)
    return returnedcolor

def pupil():
    evan.fillcolor("white")
    evan.pendown()
    evan.begin_fill()
    evan.circle(20)
    evan.end_fill()
    evan.penup()

def eyeball():
    evan.fillcolor("black")
    evan.pendown()
    evan.begin_fill()
    evan.circle(60)
    evan.end_fill()
    evan.penup()

def ear():
    evan.pendown()
    evan.fillcolor("yellow")
    evan.begin_fill()
    for i  in [0,1]:
        evan.forward(250)
        evan.right(90)
        evan.forward(70)
        evan.right(90)
    evan.end_fill()
    evan.penup()

def eartip():
    evan.pendown()
    evan.fillcolor("black")
    evan.begin_fill()
    for i in [0,1]:
        evan.forward(70)
        evan.right(90)
    evan.end_fill()
    evan.penup()

def cheek():
    evan.fillcolor(col)
    evan.begin_fill()
    evan.circle(50)
    evan.end_fill()
    evan.penup()

def head():
    evan.penup()
    evan.goto(0,-350)
    evan.pendown()
    evan.fillcolor("yellow")
    evan.begin_fill()
    evan.circle(300)
    evan.end_fill()
    evan.penup()

def nose():
    evan.goto(0,-75)
    evan.pendown()
    evan.fillcolor("black")
    evan.begin_fill()
    evan.circle(10)
    evan.end_fill()
    evan.penup()

def mouth():
    evan.goto(-50,-125)
    evan.pendown()
    evan.fillcolor("black")
    evan.begin_fill()
    for i  in [0,1]:
        evan.forward(100)
        evan.right(90)
        evan.forward(50)
        evan.right(90)
    evan.end_fill()
    evan.penup()
    
def toungue():
    evan.goto(0,-175)
    evan.fillcolor("red")
    evan.pendown()
    evan.begin_fill()
    evan.left(90)
    evan.forward(25)
    for i in [0,1]:
        evan.right(90)
        evan.forward(50)
        evan.right(90)
        evan.forward(25)
    evan.end_fill()
    evan.penup()

def bolt(color):
    evan.goto(-385, -150)
    evan.fillcolor(color)
    evan.pendown()
    evan.begin_fill()
    evan.forward(25)
    evan.right(135)
    evan.forward(60)
    evan.right(230)
    evan.forward(15)
    evan.right(135)
    evan.forward(80)
    evan.right(160)
    evan.forward(60)
    evan.left(110)
    evan.forward(10)
    evan.right(120)
    evan.forward(55)
    evan.right(70)
    evan.forward(12)
    evan.end_fill()
    evan.penup()

def cloud(color):
    evan.goto(-350, -105)
    evan.fillcolor(color)
    evan.pendown()
    evan.begin_fill()
    for i in [0,1]:
        evan.circle(20,180)
        evan.forward(10)
        evan.right(90)
    for i in [0,1]:
        evan.right(90)
        evan.circle(20,180)
        evan.forward(10)
    evan.left(14)
    evan.forward(88)
    evan.end_fill()
    evan.penup()
    
import turtle
import random
wn = turtle.Screen()
evan = turtle.Turtle()
evan.speed(10)    

#head unique features
head()
nose()
mouth()
toungue()

#left eye and pupil
evan.goto(-75, 75)
eyeball()
evan.goto(-115, 105)
pupil()
#right eye and pupil
evan.goto(150, 75)
eyeball()
evan.goto(115, 105)
pupil()

#left ear and tip
evan.goto(-230, 135)
evan.left(35)
ear()
evan.goto(-331.5, 283)
eartip()

#Fix Angle of pen
evan.right(255)

#Right ear and tip
evan.goto(190, 165)
ear()
evan.goto(350, 358)
evan.right(90)
eartip()

#Fix Angle of Pen
evan.right(135)

#colourmode setup and randomcolor function called
wn.colormode(255)
col = randomColor()

#left and right cheek
evan.goto(-170, -150)
cheek()
evan.goto(170,-150)
cheek()

#Lightning Bolt drawing PARAMETER Function #1
bolt(col)

#Cloud drawing PARAMETER Function #2
cloud(col)

wn.exitonclick()
