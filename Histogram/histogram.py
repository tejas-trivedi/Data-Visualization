import plotly.express as plot
import numpy as np

np.random.seed(20)

# declaring size of the array
size = 40

data = np.random.randint(low=0, high=120, size=size)
fig = plot.histogram(x=data, labels={'x': 'data', 'y': 'count'})

fig.layout.template = 'plotly_dark'
fig.update_layout(
    title='Histogram Plot',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    xaxis_tickangle=-30,
    width=500,
    height=500,
    autosize=True,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()