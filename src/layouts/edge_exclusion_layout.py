from dash import dcc, html

import ids


edge_exclusion_layout = html.Div([
    html.H6("Edge Exclusion"),
    html.Div([
        html.H6("Overlay:"),
        dcc.RadioItems(
            id=ids.RadioItems.EDGE_EXCLUSION_STATE,
            options=[
                {"label": "On", "value": True},
                {"label": "Off", "value": False},
            ],
            inline=True,
            style={"alignItems": "right", "width": "200px"},
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),

    
    html.Div([
        html.H6("Type:"),
        dcc.RadioItems(
            id=ids.RadioItems.EDGE_EXCLUSION_TYPE,
            options=[
                {"label": "Uniform", "value": "uniform"},
                {"label": "Radial", "value": "radial"},
            ],
            inline=True,
            style={"alignItems": "right", "width": "200px"},
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),

    
    html.Div([
        html.H6("Distance:"),
        dcc.Input(
            id=ids.Input.EDGE_EXCLUSION_DISTANCE,
            type="number",
            step=0.1,
            debounce=True,
        )
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
