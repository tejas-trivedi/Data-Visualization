import plotly.graph_objects as go
import numpy as np

np.random.seed(45)

# declaring size of arr
size = 5

x = [f'Product {i}' for i in range(size)]
y = np.random.randint(low=0, high=100, size=size)

# creating a Pie Chart
fig = go.Figure(data=[go.Pie(labels=x, values=y)])

fig.layout.template = 'plotly_dark'
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    title='Pie Chart',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    width=500,
    height=500,
    autosize=False,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()