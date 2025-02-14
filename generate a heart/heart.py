# import math
# from turtle import *

# k =  turtle.Turtle()
# shape ("turtle")
# Turtle().screen.delay(0)


# def hearta(k):
#     return 15 * math.sin(k) ** 3

# def heartb(k):
#     return 11.8 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# speed(0)
# pensize(2)
# bgcolor("black")


# for i in range(10000):
#     x = hearta(i) * 20
#     y = heartb(i) * 20
#     goto(x, y)
#     for j in range (5):
#         goto(x, 0)
#         color("red")

# turtle.done()




# deepseek
# import math
# from turtle import *

# # Set up the turtle
# k = Turtle()
# k.shape("turtle")
# k.speed(0)
# k.pensize(2)
# k.color("cyan")
# Screen().bgcolor("black")

# # Define the heart functions
# def hearta(t):
#     return 15 * math.sin(t) ** 3

# def heartb(t):
#     return 12 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

# # Draw the heart
# for i in range(600):
#     t = i * 0.1  # Scale the parameter to get a smoother curve
#     x = hearta(t) * 17
#     y = heartb(t) * 17
#     k.goto(x, y)

# # Finish drawing
# k.hideturtle()
# done()



import math
import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color("red")
pen.hideturtle()

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 4 * math.cos(3 * k) - math.cos(4 * k)

# Smooth range for heart shape
pen.up()
for k in [i * 3 for i in range(0, 200)]:  # 0 to 2π in small steps
    x = hearta(k) * 20
    y = heartb(k) * 20
    pen.goto(x, y)
    pen.down()

# Complete drawing
turtle.done()