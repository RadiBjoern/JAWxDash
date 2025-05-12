from dash import dcc, html

import ids
from templates.offset_template import MAPPATTERN_OFFSET, SAMPLE_OFFSET


def get_input_div(info:dict) -> html.Div:
    return html.Div([
        html.H6(info["label"]),
        dcc.Input(
            id=info["id"],
            value=info["value"],
            #placeholder=info["placeholder"],
            debounce=True,
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"})


map_pattern_info = [
    {
        "label": "X:",
        "id": ids.Offset.MAPPATTERN_X,
        "value": MAPPATTERN_OFFSET["x"]
    },
    {
        "label": "Y:",
        "id": ids.Offset.MAPPATTERN_Y,
        "value": MAPPATTERN_OFFSET["y"]
    },
    {
        "label": "Theta:",
        "id": ids.Offset.MAPPATTERN_THETA,
        "value": MAPPATTERN_OFFSET["theta"]
    },
]
map_pattern_div = [get_input_div(setting) for setting in map_pattern_info]


sample_info = [
    {
        "label": "X:",
        "id": ids.Offset.SAMPLE_X,
        "value": SAMPLE_OFFSET["x"]
    },
    {
        "label": "Y:",
        "id": ids.Offset.SAMPLE_Y,
        "value": SAMPLE_OFFSET["y"]
    },
    {
        "label": "Theta:",
        "id": ids.Offset.SAMPLE_THETA,
        "value": SAMPLE_OFFSET["theta"]
    },
]
sample_div = get_input_div(sample_info)


offset_layout = html.Div(
    [
        ### MapPattern Offset ###
        html.H6("MapPattern Offset"),
        html.Div(map_pattern_div),


        ### Sample offset ###
        html.H6("Sample Offset"),
        html.Div(sample_div),
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
