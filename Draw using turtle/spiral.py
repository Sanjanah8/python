import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Draw a Spiral")
t = turtle.Turtle()

# Draw a spiral
t.speed(10)  # Set the speed to fast
for i in range(100):
    t.forward(i * 10)
    t.right(45)

# Complete drawing
turtle.done()
