# Package import
from dash import html, dcc
import plotly.express as px


# Local import
import ids
from sample_outlines import sample_outlines



sample_layout = html.Div([

    # colormaps
    html.H6("Colormap", style={'textAlign': 'center',}),
    dcc.Dropdown(
        id=ids.DropDown.COLORMAPS,
        options=sorted([colorscale for colorscale in px.colors.named_colorscales()]),
        value='viridis',
        multi=False,
        clearable=False,
    ),


    # sample_outline
    html.H6("Sample outline", style={'textAlign': 'center',}),
    dcc.Dropdown(
        id=ids.DropDown.SAMPLE_OUTLINE,
        options=list(sample_outlines.keys()),
        multi=False,
        clearable=True,
    ),


    # z_data
    html.H6("Z-Data", style={'textAlign': 'center',}),
    dcc.Dropdown(
        id=ids.DropDown.Z_DATA,
        options=[],
        value='',
        multi=False,
        clearable=False,
    ),
])

