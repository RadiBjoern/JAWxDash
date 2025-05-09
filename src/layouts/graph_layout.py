from dash import dcc
import plotly.graph_objs as go


import ids

from templates.graph_template import FIGURE_LAYOUT


# Base template for the figure
figure = go.Figure(
    layout=go.Layout(
        FIGURE_LAYOUT
    ),
)

# Adding a placeholder for colormap
figure.add_trace(go.Scatter(
        x=[None],
        y=[None],
        name='colormap_placeholder',
))


graph_layout = dcc.Graph(
    id=ids.Graph.MAIN, 
    style={'height': '900px', 'width': '100%'},
    figure=figure,
)