import plotly.express as plot
import numpy as np
import pandas as pd

size = 20
data = np.random.randint(low=0, high=25, size=size)

df = pd.DataFrame(dict(
    linear=data,
    inclusive=data,
    exclusive=data
)).melt(var_name="quartilemethod")


fig = plot.box(df, y="value", facet_col="quartilemethod", color="quartilemethod",
             boxmode="overlay", points='all')
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

fig.update_traces(quartilemethod="linear", jitter=0, col=1)
fig.update_traces(quartilemethod="inclusive", jitter=0, col=2)
fig.update_traces(quartilemethod="exclusive", jitter=0, col=3)

fig.show()