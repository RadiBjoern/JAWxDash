# Package import
from dash import html, dcc
import logging


# Local import
import ids
from utils.sample_outlines import sample_outlines


logger = logging.getLogger(__name__)


sample_layout = html.Div(
    [
        html.H6("Sample"),

        # colormaps
        html.Div(
            [
                html.H6("Colormap:", style={"marginRight": "10px"}),
                dcc.Dropdown(
                    id=ids.DropDown.COLORMAPS,
                    multi=False,
                    clearable=False,
                    style={"alignItems": "right", "width": "200px"},
                ),
            ], 
            style={"display": "flex", "alignItems": "center", "gap": "10px"}
        ),


        # sample_outline
        html.Div([
            html.H6("Outline:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id=ids.DropDown.SAMPLE_OUTLINE,
                options=list(sample_outlines.keys()),
                multi=False,
                clearable=True,
                style={"width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),


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

