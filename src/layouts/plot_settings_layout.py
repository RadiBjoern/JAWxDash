from dash import dcc, html
import dash_bootstrap_components as dbc
import logging

from src import ids


logger = logging.getLogger(__name__)


spot_layout = dbc.Card([
    dbc.CardHeader("Plot Settings"),
    dbc.CardBody([
        # Z data
        dbc.Row([
            dbc.Col(
                html.Label("Z-Data", className="mb-0 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=ids.DropDown.Z_DATA,
                    options=[],
                    multi=False,
                    clearable=False,
                    className="mb-0",
                ),
                width=7,
            )
        ]),

        # Colormap
        dbc.Row([
            dbc.Col(
                html.Label("Colormap", className="mb-0 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=ids.DropDown.COLORMAPS,
                    multi=False,
                    clearable=False,
                    className="mb-0",
                ),      
                width=7,          
            )
        ]),

        # Marker style
        dbc.Row([
            dbc.Col(
                html.Label("Marker style", className="mb-0 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.RadioItems(
                    id=ids.RadioItems.PLOT_STYLE,
                    options=[
                       {'label': 'PTS', 'value': 'point'},
                       {'label': 'ELL', 'value': 'ellipse'},
                    ],
                    inline=True,
                    labelStyle={"margin-right": "15px"},
                    className="mb-0",
                ),
                width=7,
            )
        ]),

        # Focus probes
        dbc.Row([
            dbc.Col(
                html.Label("Probes", className="mb-0 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.RadioItems(
                    id=ids.RadioItems.SPOT_SIZE,
                    options=[
                        {'label': 'ON', 'value': 0.03},
                        {'label': 'OFF', 'value': 0.3},
                    ],
                    inline=True,
                    labelStyle={"margin-right": "15px"},
                    className="mb-0",
                ),
                width=7,
            )
        ]),

        # Angle of incident
        dbc.Row(
            html.Label("Angle of incident (deg)", style={'textAlign': 'center',}),
        ),
        dbc.Row(
            dcc.Slider(
                id=ids.Slider.ANGLE_OF_INCIDENT, 
                min=45, 
                max=85, 
                step=1, 
                marks={i: str(i) for i in range(45, 86, 5)},
                className="mb-0",
            ),
        )

    ])
], className="mt-1")

