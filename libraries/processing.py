from processing import *

def setup():
    size(400, 400)
    background(255)

def draw():
    fill(0, 100, 255)
    ellipse(mouseX, mouseY, 50, 50)
