import turtle

def draw_snowflake(turtle_obj, length):
    for _ in range(6):
        draw_koch_curve(turtle_obj, length)
        turtle_obj.right(60)

def draw_koch_curve(turtle_obj, length):
    if length < 10:
        turtle_obj.forward(length)
    else:
        length /= 3.0
        draw_koch_curve(turtle_obj, length)
        turtle_obj.left(60)
        draw_koch_curve(turtle_obj, length)
        turtle_obj.right(120)
        draw_koch_curve(turtle_obj, length)
        turtle_obj.left(60)
        draw_koch_curve(turtle_obj, length)

screen = turtle.Screen()
screen.bgcolor("white")
snowflake = turtle.Turtle()
snowflake.speed(0)
draw_snowflake(snowflake, 300)
turtle.done()
