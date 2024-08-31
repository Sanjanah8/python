import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Draw a Star")
t = turtle.Turtle()

# Draw a star
for _ in range(5):
    t.forward(100)
    t.right(144)  # Turn right by 144 degrees

# Complete drawing
turtle.done()
