import turtle
import time

a = 0
b = 0

turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup() # nie rysuje podczas przemieszczenia
turtle.goto(0, 160)
turtle.pendown() # rysuje podczas przemieszczenia

while True:

    turtle.forward(a)
    turtle.right(b)
    a += 3
    b += 1
    time.sleep(0.5) #w sekundach

    if b==50:
        turtle.pencolor("red")
    if b==100:
        turtle.pencolor("blue")
    if b == 200:
        print(b)
        break

turtle.exitonclick()
