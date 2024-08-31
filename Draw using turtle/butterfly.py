import turtle

def draw_butterfly():
    screen = turtle.Screen()
    screen.title("Draw a Butterfly")
    t = turtle.Turtle()
    t.speed(10)
    
    # Draw butterfly wings
    t.color("red")
    t.begin_fill()
    t.circle(100, 180)
    t.circle(100, -180)
    t.end_fill()

    t.right(90)
    t.color("blue")
    t.begin_fill()
    t.circle(80, 180)
    t.circle(80, -180)
    t.end_fill()

    # Draw body
    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    turtle.done()

draw_butterfly()
