import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Maze Game")
screen.setup(700, 700)

#This is my pen class, it is used to create an object
class Pen(turtle.Turtle):
    #__init__ is a initializer that classes need on how they begin their life
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXX            XXXX",
"X  XXXXXX   XXXXXXX  XXXX",
"X      XX   XXXXXXX    XX",
"X      XX   XXX        XX",
"XXXXX  XX   XXX        XX",
"XXXXX  XX   XXXXXX  XXXXX",
"XXXXX  XX     XXXX  XXXXX",
"X  XX         XXXX  XXXXX",
"X  XX  XXXXXXXXXXXXXXXXXX",
"X        XXXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX  XXXXX  X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XXX  XXXXX              X",
"XXX  XXXXXXXXXXXXX  XXXXX",
"XXX   XXXXXXXXXXXX  XXXXX",
"XXX        XXXXX        X",
"XXXXX                   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)

#create a setup function for a level
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

pen = Pen()

setup_maze(levels[1])

while True:
    pass