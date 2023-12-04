from turtle import *
import turtle
import time

screen = turtle.Screen()
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.shape("turtle")
t.color("darkorange")


def draw_petal():
    t.begin_fill()
    t.color("yellow")
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)
    t.end_fill()

def draw_stem():
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("green")
    t.pensize(17)
    t.setheading(270)
    t.forward(150)
    t.pensize(1)
    t.color("darkorange")

draw_stem()

t.penup()
t.goto(0, 0)
t.pendown()
angle = 360/12
for _ in range(12):
    draw_petal()
    t.left(30)

t.penup()
t.goto(-40,0)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(45)
t.end_fill()
t.penup()
t.hideturtle()
time.sleep(1)

t.goto(0,-180)
t.pendown
t.color("red")
t.write("Para nadie :)", align="center", font=("Arial", 16, "bold"))
t.hideturtle()
turtle.done()
