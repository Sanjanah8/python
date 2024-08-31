import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Interactive Drawing")
t = turtle.Turtle()

# Define movement functions
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def clear_screen():
    t.clear()

# Set up key bindings
screen.listen()
screen.onkey(move_forward, "w")   # Move forward with 'w'
screen.onkey(move_backward, "s")  # Move backward with 's'
screen.onkey(turn_left, "a")      # Turn left with 'a'
screen.onkey(turn_right, "d")     # Turn right with 'd'
screen.onkey(clear_screen, "c")   # Clear screen with 'c'

# Start the turtle graphics loop
turtle.done()
