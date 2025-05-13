from dash import dcc, html, callback, Output, Input

import ids
from templates.offset_template import MAPPATTERN_OFFSET, SAMPLE_OFFSET


def get_input_div(info:dict) -> html.Div:
    return html.Div([
        html.H6(info["label"]),
        dcc.Input(
            id=info["id"],
            #placeholder=info["placeholder"],
            debounce=True,
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"})


map_pattern_info = [
    {"label": "X:", "id": ids.Offset.MAPPATTERN_X},
    {"label": "Y:", "id": ids.Offset.MAPPATTERN_Y},
    {"label": "Theta:", "id": ids.Offset.MAPPATTERN_THETA},
]
map_pattern_div = [get_input_div(setting) for setting in map_pattern_info]


sample_info = [
    {"label": "X:", "id": ids.Offset.SAMPLE_X},
    {"label": "Y:", "id": ids.Offset.SAMPLE_Y},
    {"label": "Theta:", "id": ids.Offset.SAMPLE_THETA},
]
sample_div = [get_input_div(setting) for setting in sample_info]


offset_layout = html.Div(
    [
        dcc.Store(
            id=ids.Store.OFFSET_MAPPATTERN_SETTINGS,
            data=MAPPATTERN_OFFSET,
            storage_type="memory",
        ),
        dcc.Store(
            id=ids.Store.OFFSET_SAMPLE_SETTINGS,
            data=SAMPLE_OFFSET,
            storage_type="memory",
        ),


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


@callback(
    Output(ids.Offset.MAPPATTERN_X, "value"),
    Output(ids.Offset.MAPPATTERN_Y, "value"),
    Output(ids.Offset.MAPPATTERN_THETA, "value"),
    Output(ids.Offset.SAMPLE_X, "value"),
    Output(ids.Offset.SAMPLE_Y, "value"),
    Output(ids.Offset.SAMPLE_THETA, "value"),
    Input(ids.Store.OFFSET_MAPPATTERN_SETTINGS, "data"),
    Input(ids.Store.OFFSET_SAMPLE_SETTINGS, "data"),
)
def load_defaults_offsets(mappattern_offset, sample_offset):
    return (
        mappattern_offset["x"],
        mappattern_offset["y"],
        mappattern_offset["theta"],
        sample_offset["x"],
        sample_offset["y"],
        sample_offset["theta"],
    )