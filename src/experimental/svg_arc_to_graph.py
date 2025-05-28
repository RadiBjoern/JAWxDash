import plotly.graph_objects as go
import numpy as np


# Generate arc path
path_str = [
    "M 3.0 15.0",
    "q 1.5 -2.0 1.5 -5.0",
    "q 0.0 -2.0 1.5 -4.0",
    "M 8.0 4.0",
    "A 8.0 8.0 0.0 0.0 1.0 12.0 6.0",
    "q 0.5 4.0 -2.0 9.0",
    "M 13.0 21.0",
    "q 1.5 -2.0 2.0 -5.0",
    "M 16.0 12.0",
    "v -1.0",
    "A 4.0 4.0 0.0 0.0 0.0 -8.0 0.0",
    "q 0.0 4.0 -2.5 7.0",
    "M 8.5 20.0",
    "q 3.0 -3.0 3.5 -9.0",
]

# Plot
fig = go.Figure()

# Add dummy trace to force layout dimensions
fig.add_trace(go.Scatter(x=[-3, 3], y=[-3, 3], mode='markers', marker=dict(color='white'), showlegend=False))

# Add the arc as shape
fig.update_layout(
    shapes=[
        dict(
            type="path",
            path=" ".join(path_str),
            line_color="blue",
            line_width=3,
        )
    ],
    width=600,
    height=600,
    xaxis=dict(range=[-3, 3], zeroline=False),
    yaxis=dict(range=[-3, 3], scaleanchor='x', zeroline=False),
)

fig.show()
