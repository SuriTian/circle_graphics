#IMPORTS
import turtle
import random
import time

turtle.color('black')
style = ('Comic Sans', 30)
turtle.write('The Never Stopping Ball Graphics', align='center')
turtle.hideturtle()

#SCREEN
screen = turtle.Screen()
screen.bgcolor('white')
screen.tracer(0)

#RECTANGULAR BORDER
border = turtle.Turtle()
border.color('black')
border.shapesize(0.01, 0.01, 0.01)
border.shape('circle')

border.penup()
border.goto(-300, -300)
border.pendown()

for i in range(4):
    border.forward(600)
    border.left(90)

#RANDOMIZER
rng = [-15, -30, -45, -60, -75, 15, 30, 45, 60, 75]

#BALL
ball = turtle.Turtle()
ball.hideturtle()
ball.speed(10)

def move(ball):
    ball.color('pink')
    ball.right(90)
    ball.forward(10)
    ball.left(90)
    ball.pendown()
    ball.begin_fill()
    ball.circle(10)
    ball.end_fill()
    ball.penup()
    ball.left(90)
    ball.forward(10)
    ball.right(90)

while True:
    ball.clear()
    degree = random.choice(rng)
    if -290 < ball.xcor() < 290 and -290 < ball.ycor() < 290:
        move(ball)
    else:
        if ball.xcor() < -290: #east
            ball.setheading(0)
        elif ball.xcor() > 290: #west
            ball.setheading(180)
        elif ball.ycor() < -290: #north
            ball.setheading(90)
        elif ball.ycor() > 290: #south
            ball.setheading(270)
        ball.left(degree)
        move(ball)
    screen.update()
    ball.forward(1)
    time.sleep(0.000001)

turtle.done()
