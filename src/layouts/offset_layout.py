from dash import dcc, html

from templates.offset_template import MAPPATTERN_OFFSET, SAMPLE_OFFSET


offset_layout = html.Div(
    [
        ### MapPattern Offset ###

        html.H6("MapPattern Offset"),
        # x-offset
        html.Div([
            html.H6("X:"),
            dcc.Input(
                placeholder=MAPPATTERN_OFFSET["x"],
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),
        # y-offset
        html.Div([
            html.H6("Y:"),
            dcc.Input(
                placeholder=MAPPATTERN_OFFSET["y"],
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),
        # theta-offset
        html.Div([
            html.H6("Theta:"),
            dcc.Input(
                placeholder=MAPPATTERN_OFFSET["theta"],
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),


        ### Sample offset ###
        html.H6("Sample Offset"),
        # x-offset
        html.Div([
            html.H6("X:"),
            dcc.Input(
                placeholder=SAMPLE_OFFSET["x"],
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),
        # y-offset
        html.Div([
            html.H6("Y:"),
            dcc.Input(
                placeholder=SAMPLE_OFFSET["y"],
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),
        # theta-offset
        html.Div([
            html.H6("Theta:"),
            dcc.Input(
                placeholder=SAMPLE_OFFSET["theta"],
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
