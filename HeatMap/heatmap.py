import plotly.express as plot
import numpy as np

np.random.seed(45)

# declaring size of the array
rows = 5
columns = 3

data = np.random.randint(low=0, high=50, size=(columns, rows))

fig = plot.imshow(data,
                labels=dict(x="X Axis Title", y="Y Axis Title", color="Productivity"),
                x=[f'Item {i}' for i in range(rows)],
                y=[f'Type {i}' for i in range(columns)],
                )

fig.layout.template = 'plotly_dark'
fig.update_xaxes(side="top")
fig.update_layout(
    title='Heat Map ',
    xaxis_tickangle=-35,
    width=500,
    height=500,
    autosize=False,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()