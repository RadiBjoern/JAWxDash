from dash import dcc, html
import dash_bootstrap_components as dbc

import ids


stage_layout = dbc.Card([
    dbc.CardHeader("Stage"),
    dbc.CardBody([
        dbc.Row([
            dbc.Col(
                html.Label("Watermark:", className="mb-2 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.RadioItems(
                    id=ids.RadioItems.STAGE_STATE,
                    options=[
                        {"label": "ON", "value": True},
                        {"label": "OFF", "value": False},
                    ],
                    inline=True,
                    className="mb-2"
                ),
                width=7,
            ),
        ]),
    ]),
], className="mt-4")
