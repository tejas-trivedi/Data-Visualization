import plotly.graph_objects as plot
import numpy as np

np.random.seed(45)

# defining size of the array
size = 10

x = [f'Item {i}' for i in range(size)]
y = np.random.randint(low=0, high=100, size=size)

fig = plot.Figure(plot.Bar(
    x=x,
    y=y,
    text=y,
    marker_color='indianred',
    hovertemplate="%{x} : %{y} <extra></extra>",
    textposition='outside',
    showlegend=False,
))

fig.layout.template = 'plotly_dark'
layout_yaxis_visible = True
layout_yaxis_showticklabels = False
fig.update_layout(
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    xaxis_tickangle=-30,
    width=500,
    height=500,
    autosize=False,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.update_yaxes(showgrid=True, showticklabels=True)

fig.show()