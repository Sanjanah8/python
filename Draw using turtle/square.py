import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Draw a Square")
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Complete drawing
turtle.done()
