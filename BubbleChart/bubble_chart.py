import plotly.graph_objects as plot
import numpy as np

np.random.seed(45)

# declaring size of the array
size = 10
size_arr = np.random.randint(low=50, high=600, size=size)

x = np.random.randint(low=0, high=30, size=size)
y = np.random.randint(low=0, high=20, size=size)

fig = plot.Figure(data=[plot.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=size_arr,
        sizemode='area',
        sizeref=2.*max(size_arr)/(40.**2),
        sizemin=4
    ),
    hovertemplate=" x : %{x} <br> y : %{y} <br>"
)])

# Adjust height and width of the image
fig.layout.template = 'plotly_dark'
fig.update_layout(
    title='Bubble Chart',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    xaxis_tickangle=-30,
    width=500,
    height=500,
    autosize=False,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)

fig.show()