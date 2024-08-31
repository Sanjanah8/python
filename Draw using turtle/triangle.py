import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Draw a Triangle")
t = turtle.Turtle()

# Draw a triangle
for _ in range(3):
    t.forward(100)  # Move forward by 100 units
    t.left(120)     # Turn left by 120 degrees

# Complete drawing
turtle.done()
