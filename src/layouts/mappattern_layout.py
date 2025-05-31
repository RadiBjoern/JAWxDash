from dash import dcc, html
import dash_bootstrap_components as dbc

import ids



row_info = [
    {"label": "X offset:", "id": ids.Input.MAPPATTERN_X},
    {"label": "Y offset:", "id": ids.Input.MAPPATTERN_Y},
    {"label": "\u03F4:", "id": ids.Input.MAPPATTERN_THETA},
]

def generate_row(label, comp_id):
    return dbc.Row([
        dbc.Col(
            html.Label(
                children=label,
                className="mb-0 d-block text-body text-decoration-none",
            ),
            width=5,
        ),
        dbc.Col(
            dcc.Input(
                id=comp_id,
                type="number",
                debounce=True,
                className="form-control mb-0"
            ),
            width=7,
        ),
    ], className="mb-0")



mappattern_layout = dbc.Card([
    dbc.CardHeader("MapPattern"),
    dbc.CardBody([
        generate_row("X offset", ids.Input.MAPPATTERN_X),
        generate_row("Y offset", ids.Input.MAPPATTERN_Y),
        generate_row("\u03F4 offset", ids.Input.MAPPATTERN_THETA),
    ])
], className="mt-1")
