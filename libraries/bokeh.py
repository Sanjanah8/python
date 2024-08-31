from bokeh.plotting import figure, show

p = figure(title="Simple Line Plot", x_axis_label='x', y_axis_label='y')
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], legend_label="Line", line_width=2)

show(p)
