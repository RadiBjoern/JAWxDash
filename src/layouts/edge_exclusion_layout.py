from dash import dcc, html
import dash_bootstrap_components as dbc

from src import ids


edge_exclusion_layout = dbc.Card([
    dbc.CardHeader("Edge Exclusion"),
    dbc.CardBody([

        # Overlay
        dbc.Row([
            dbc.Col([
                html.Label("Overlay", className="mb-0 d-block text-body text-decoration-none"),
            ], width=5),
            dbc.Col([
                dcc.RadioItems(
                    id=ids.RadioItems.EDGE_EXCLUSION_STATE,
                    options=[
                        {"label": "ON", "value": True},
                        {"label": "OFF", "value": False},
                    ],
                    inline=True,
                    labelStyle={"margin-right": "15px"},
                    className="mb-0"
                )
            ], width=7)
        ]),

        # Type
        dbc.Row([
            dbc.Col([
                html.Label("Type", className="mb-0 d-block text-body text-decoration-none"),
            ], width=5),
            dbc.Col([
                dcc.RadioItems(
                    id=ids.RadioItems.EDGE_EXCLUSION_TYPE,
                    options=[
                        {"label": "RAD", "value": "radial"},
                        {"label": "UNI", "value": "uniform"},
                    ],
                    inline=True,
                    labelStyle={"margin-right": "15px"},
                    className="mb-0"
                )
            ], width=7)
        ]),

        # Distance
        dbc.Row([
            dbc.Col([
                html.Label("Distance", className="mb-0 d-block text-body text-decoration-none"),
            ], width=5),
            dbc.Col([
                dcc.Input(
                    id=ids.Input.EDGE_EXCLUSION_DISTANCE,
                    type="number",
                    step=0.1,
                    debounce=True,
                    className="form-control mb-0",
                )
            ], width=7)
        ]),

        # Excluded points
        dbc.Row([
            dbc.Col([
                html.Label("Excl. pts", className="mb-0 d-block text-body text-decoration-none"),
            ], width=5),
            dbc.Col([
                html.H6(id=ids.Text.EXCLUDED_POINTS),
            ], width=7)
        ]),

        # Batch proc.
        dbc.Row([
            dbc.Col([
                html.Label("Batch proc.", className="mb-0 d-block text-body text-decoration-none"),
            ], width=5),
            dbc.Col([
                dcc.RadioItems(
                    id=ids.RadioItems.BATCH_PROCESSING,
                    options=[
                        {"label": "ON", "value": True},
                        {"label": "OFF", "value": False},
                    ],
                    inline=True,
                    labelStyle={"margin-right": "15px"},
                    className="mb-0",
                ),
            ], width=7)
        ]),

        # Vertical spacing
        html.Div(style={"height": "10px"}),

        # Download btn
        dbc.Row([
            dbc.Button(
                "Download Masked Data",
                id=ids.Button.DOWNLOAD_MASKED_DATA,
                color="primary",
                className="mb-0 w-100"
            ),
            dcc.Download(id=ids.Download.EDGE_EXCLUDED_FILE)
        ]),
    ])
], className="mt-1")
