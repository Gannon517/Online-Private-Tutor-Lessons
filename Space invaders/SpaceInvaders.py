import turtle
import math
import random
import winsound

#drawing screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space_invaders_background.gif")
screen.tracer(0)

#register other shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#drawing border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
scoreString = "Score: {}".format(score)
score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create a player 
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#speeds
player.speed = 0
enemySpeed = 0.2

#create enemies list
numEnemies = 30
enemies = []

#add to my list
for i in range(numEnemies):
    #create enemy
    enemies.append(turtle.Turtle())

enemyStartX = -225
enemyStartY = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemyStartX + (50*enemy_number)
    y = enemyStartY
    enemy.setposition(x, y)
    enemy_number+=1
    if enemy_number == 10:
        enemyStartY -= 50
        enemy_number = 0


#create the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 7

#define bullet state
bulletState = "ready"

def left():
    player.speed = -1
    

def right():
    player.speed = 1

def move():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.goto(x, -250)

def fireBullet():
    global bulletState
    if bulletState == "ready":
        playSound("laser.wav")
        bulletState = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y+10)
        bullet.showturtle()

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 15:
        return True
    return False

def playSound(file, time=0):
    winsound.PlaySound(file, winsound.SND_ASYNC)

#keyboard bindings
screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(fireBullet, "space")

#Main game loop
while True:
    screen.update()
    move()
    
    for enemy in enemies:
        #move enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        #reverse enemy direction and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1
        
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        #check for collision of bulelt and enemy
        if isCollision(bullet, enemy):
            playSound("explosion.wav")
            #reset bullet
            bullet.hideturtle
            bulletState = "ready"
            bullet.setposition(0, -400)
            #Get rid of enemy
            enemy.setposition(0, 10000)
            #update score
            score+=10
            scoreString = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
        
        if isCollision(player, enemy):
            playSound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break

    #move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #bullet border collision
    if bullet.ycor() > 285:
        bullet.hideturtle()
        bulletState = "ready"

    if score == 300:
        print("You have won!")
        break
        
