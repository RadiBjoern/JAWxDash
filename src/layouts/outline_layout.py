from dash import dcc, html

import ids
from utils.sample_outlines import sample_outlines




def get_input_div(info:dict) -> html.Div:
    return html.Div([
        html.H6(info["label"]),
        dcc.Input(
            id=info["id"],
            type="number",
            debounce=True,
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"})



outline_info = [
    {"label": "X:", "id": ids.Input.SAMPLE_X},
    {"label": "Y:", "id": ids.Input.SAMPLE_Y},
    {"label": "\u03F4:", "id": ids.Input.SAMPLE_THETA},
    {"label": "R", "id": ids.Input.SAMPLE_RADIUS},
    {"label": "W", "id": ids.Input.SAMPLE_WIDTH},
    {"label": "H", "id": ids.Input.SAMPLE_HEIGHT},
]
outline_div = [get_input_div(setting) for setting in outline_info]



outline_layout = html.Div(
    [
        ### Sample offset ###
        html.H6("Sample Outline"),

        # sample_outline
        html.Div([
            html.H6("Outline:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id=ids.DropDown.SAMPLE_OUTLINE,
                options=sample_outlines,
                multi=False,
                clearable=True,
                style={"width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),


        # Offset
        html.Div(outline_div),
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
