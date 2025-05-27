import plotly.graph_objects as go

fig = go.Figure()

# Add a shape (e.g. rectangle)
fig.add_shape(
    type="rect",
    x0=1, y0=1, x1=2, y1=2,
    line=dict(color="RoyalBlue"),
    fillcolor="RoyalBlue"
)

# Add a dummy scatter trace with colorbar
fig.add_trace(go.Scatter(
    x=[None],  # No visible point
    y=[None],
    mode='markers',
    marker=dict(
        color=[0],  # dummy value
        colorscale='Viridis',
        cmin=0,
        cmax=123,
        colorbar=dict(title="Value"),
        showscale=True,
        size=0  # no visible marker
    ),
    hoverinfo='skip',
    showlegend=False
))

fig.update_layout(
    title="Shape with Colorbar (Dummy Scatter)",
    xaxis=dict(range=[0, 5]),
    yaxis=dict(range=[0, 5])
)

fig.show()
