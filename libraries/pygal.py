import pygal

line_chart = pygal.Line()
line_chart.title = 'Browser Usage'
line_chart.add('Chrome', [1, 2, 3, 4, 5])
line_chart.add('Firefox', [2, 3, 4, 5, 6])
line_chart.render_to_file('line_chart.svg')
