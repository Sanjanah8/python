import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Draw Pattern of Squares")
t = turtle.Turtle()

# Draw a pattern of squares
for _ in range(36):
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)  # Turn slightly for the pattern effect

# Complete drawing
turtle.done()
