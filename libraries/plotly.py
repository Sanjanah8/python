import plotly.graph_objects as go

# Create a simple scatter plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='markers'))
fig.update_layout(title='Interactive Scatter Plot', xaxis_title='X Axis', yaxis_title='Y Axis')
fig.show()
