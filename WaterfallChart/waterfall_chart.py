import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "20",
    orientation = "v",
    measure = ["relative", "relative", "relative", "relative", "relative", "total"],
    x = ["Exp1", "Exp2", "Exp3", "Exp4", "Exp5", "Exp6"],
    textposition = "outside",
    text = ["80", "60", "150", "220", "75", "Total"],
    y = [80, +60, 150, 220, 75, 0  ],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    increasing = {"marker":{"color":"green"}},
    totals = {"marker":{"color":"blue"}}
))

fig.update_layout(
        title = "Waterfall Chart",
        showlegend = True ,
        xaxis_title='X Axis Title',
        yaxis_title='Y Axis Title',
        width=500,
        height=500,
)
fig.layout.template = 'plotly_dark'
fig.show()