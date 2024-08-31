import pyglet

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2i', (50, 50, 200, 200)))

pyglet.app.run()
