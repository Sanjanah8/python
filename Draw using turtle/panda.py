import turtle

def draw_circle(turtle, color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_panda():
    screen = turtle.Screen()
    screen.title("Draw a Panda")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)

    # Draw face
    draw_circle(t, "white", 100, 0, -100)

    # Draw eyes
    draw_circle(t, "black", 20, -40, -20)
    draw_circle(t, "black", 20, 40, -20)
    draw_circle(t, "white", 10, -40, -10)
    draw_circle(t, "white", 10, 40, -10)

    # Draw nose
    draw_circle(t, "black", 10, 0, -40)
    
    # Draw mouth
    t.penup()
    t.goto(-10, -50)
    t.pendown()
    t.right(90)
    t.circle(10, 180)
    
    # Draw ears
    draw_circle(t, "black", 30, -70, 50)
    draw_circle(t, "black", 30, 70, 50)
    draw_circle(t, "white", 20, -70, 70)
    draw_circle(t, "white", 20, 70, 70)

    turtle.done()

draw_panda()
