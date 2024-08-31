import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Draw Concentric Circles")
t = turtle.Turtle()

# Draw concentric circles
for i in range(10, 150, 10):
    t.penup()       # Lift the pen to move without drawing
    t.goto(0, -i)   # Move to starting position of the circle
    t.pendown()     # Lower the pen to draw
    t.circle(i)     # Draw a circle with radius i

# Complete drawing
turtle.done()
