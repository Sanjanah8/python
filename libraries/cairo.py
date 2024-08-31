import cairo

WIDTH, HEIGHT = 256, 256

with cairo.SVGSurface("example.svg", WIDTH, HEIGHT) as surface:
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(0, 0, 0)
    ctx.paint()
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.move_to(10, 10)
    ctx.line_to(200, 200)
    ctx.stroke()
