from dash import dcc, html
import logging

import ids


logger = logging.getLogger(__name__)


spot_layout = html.Div(
    [
        html.H6("Beam Settings"),


        # z_data
        html.Div([
            html.H6("Z-Data:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id=ids.DropDown.Z_DATA,
                options=[],
                multi=False,
                clearable=False,
                style={"width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),


        # colormaps
        html.Div([
            html.H6("Colormap:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id=ids.DropDown.COLORMAPS,
                multi=False,
                clearable=False,
                style={"alignItems": "right", "width": "200px"},
            ),
        ], 
        style={"display": "flex", "alignItems": "center", "gap": "10px"}),


        # Marker style
        html.Div([
            html.H6("Marker style:"),
            dcc.RadioItems(
                id=ids.RadioItems.PLOT_STYLE,
                options=[
                   {'label': 'Point', 'value': 'point'},
                   {'label': 'Ellipse', 'value': 'ellipse'},
                ],
                inline=True,
                style={"alignItems": "right", "width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),


        # Angle of incident
        html.H6("Angle of incident (deg)", style={'textAlign': 'center',}),
        dcc.Slider(
            id=ids.Slider.ANGLE_OF_INCIDENT, 
            min=45, 
            max=85, 
            step=1, 
            marks={i: str(i) for i in range(45, 86, 5)},
        ),


        # Focus probes
        html.Div([
            html.H6("Focus probe", style={"marginRight": "10px"}),
            dcc.RadioItems(
                id=ids.RadioItems.SPOT_SIZE,
                options=[
                    {'label': 'ON', 'value': 0.3},
                    {'label': 'OFF', 'value': 0.03},
                ],
                inline=True,
                style={"alignItems": "right", "width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"})
    ],
    style={
        'width': '100%',
        #'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'borderRadius': '10px',
        'textAlign': 'center',
        'margin': '10px'
    },
)

