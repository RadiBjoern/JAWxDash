from dash import dcc, html
import logging

import ids


logger = logging.getLogger(__name__)


spot_layout = html.Div(
    [
        html.H6("Beam Settings"),
        html.Div([
            html.H6("Style:"),
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

    
        html.H6("Angle of incident (deg)", style={'textAlign': 'center',}),
        dcc.Slider(
            id=ids.Slider.ANGLE_OF_INCIDENT, 
            min=45, 
            max=85, 
            step=1, 
            marks={i: str(i) for i in range(45, 86, 5)},
        ),


        html.Div([
            html.H6("Size", style={"marginRight": "10px"}),
            dcc.RadioItems(
                id=ids.RadioItems.SPOT_SIZE,
                options=[
                    {'label': 'wo. FP', 'value': 0.3},
                    {'label': 'w. FP', 'value': 0.03},
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

