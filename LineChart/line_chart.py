import plotly.graph_objects as plot
import numpy as np

np.random.seed(45)

# defining size of the array
size = 10

x = np.arange(10)
y = x ** 2

fig = plot.Figure(data = plot.Scatter(x=x, y=x**2))

fig.layout.template = 'plotly_dark'
fig.update_layout(
    title='Line Chart',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    autosize=True,
    height=500,
    width=500,
    xaxis_tickangle=-30,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()