from dash import dcc, html
import dash_bootstrap_components as dbc


import ids
from utils.sample_outlines import sample_outlines


row_info = [
    {"label": "X offset", "id": ids.Input.SAMPLE_X},
    {"label": "Y offset", "id": ids.Input.SAMPLE_Y},
    {"label": "\u03F4 offset", "id": ids.Input.SAMPLE_THETA},
    {"label": "Radius", "id": ids.Input.SAMPLE_RADIUS},
    {"label": "Width", "id": ids.Input.SAMPLE_WIDTH},
    {"label": "Height", "id": ids.Input.SAMPLE_HEIGHT},
]

def generate_row(label, comp_id):
    return dbc.Row([
        dbc.Col(
            html.Label(
                children=label,
                className="mb-1 d-block text-body text-decoration-none",
            ),
            width=5,
        ),
        dbc.Col(
            dcc.Input(
                id=comp_id,
                type="number",
                debounce=True,
                className="form-control mb-1"
            ),
            width=7,
        ),
    ], className="mb-1")


outline_layout = dbc.Card([
    ### Sample offset ###
    dbc.CardHeader("Sample"),
    dbc.CardBody([

        # Sample_outline
        dbc.Row([
            dbc.Col(
                html.A(
                    "Outline:", 
                    className="mb-2 d-block text-body text-decoration-none"
                ),
                width=5
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=ids.DropDown.SAMPLE_OUTLINE,
                    options=sample_outlines,
                    multi=False,
                    clearable=True,
                    className="mb-2",
                ),
                width=7
            ),
        ], className="mb-2"),   

        generate_row("X offset", ids.Input.SAMPLE_X),
        generate_row("Y offset", ids.Input.SAMPLE_Y),
        generate_row("\u03F4 offset", ids.Input.SAMPLE_THETA),
        generate_row("Radius", ids.Input.SAMPLE_RADIUS),
        generate_row("Width", ids.Input.SAMPLE_WIDTH),
        generate_row("Height", ids.Input.SAMPLE_HEIGHT),
        
    ]),
], className="mt-4")
