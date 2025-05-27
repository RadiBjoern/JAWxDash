from dash import dcc, html


import ids



def get_input_div(info:dict) -> html.Div:
    return html.Div([
        html.H6(info["label"]),
        dcc.Input(
            id=info["id"],
            type="number",
            debounce=True,
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"})



map_pattern_info = [
    {"label": "X:", "id": ids.Input.MAPPATTERN_X},
    {"label": "Y:", "id": ids.Input.MAPPATTERN_Y},
    {"label": "\u03F4:", "id": ids.Input.MAPPATTERN_THETA},
]
map_pattern_div = [get_input_div(setting) for setting in map_pattern_info]


mappattern_layout = html.Div(
    [
        ### MapPattern Offset ###
        html.H6("MapPattern Offset"),
        html.Div(map_pattern_div),
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
