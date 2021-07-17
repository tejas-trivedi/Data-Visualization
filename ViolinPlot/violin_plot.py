import plotly.express as plot

dataframe = plot.data.tips()

fig = plot.violin(dataframe, y="total_bill",
                box=True, # draw box plot inside the violin
                points='all', # can be 'outliers', or False
               )
fig.layout.template = 'plotly_dark'
fig.update_layout(
    title='Violin Plot',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    xaxis_tickangle=-30,
    width=500,
    height=500,
    autosize=True,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()