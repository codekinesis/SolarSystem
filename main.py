from turtle import *

speed(0) # Draw animation time

bgcolor("black")

# Create the ORANGE planet
color("orange")
begin_fill()
circle(60)
end_fill()

# Moves forward
penup()
forward(100)
pendown()

# Create the GREY planet
color("grey")
begin_fill()
circle(20)
end_fill()

# Move forwards
penup()
forward(80)
pendown()

# Create RED planet
color("red")
begin_fill()
circle(40)
end_fill()

# Move forward
penup()
forward(90)
pendown()

# Create GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

# Hides Turtle at the end and keeps the GREEN planet from looking like a chat bubble
penup()
forward(30)
color("black")
done()