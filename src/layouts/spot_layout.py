from dash import dcc, html
import dash_bootstrap_components as dbc
import logging

import ids


logger = logging.getLogger(__name__)


spot_layout = dbc.Card([
    dbc.CardHeader("Beam Settings"),
    dbc.CardBody([
        # Z data
        dbc.Row([
            dbc.Col(
                html.A("Z-Data:", className="mb-2 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=ids.DropDown.Z_DATA,
                    options=[],
                    multi=False,
                    clearable=False,
                    className="mb-2",
                ),
                width=7,
            )
        ]),

        # Colormap
        dbc.Row([
            dbc.Col(
                html.A("Colormap:", className="mb-2 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=ids.DropDown.COLORMAPS,
                    multi=False,
                    clearable=False,
                    className="mb-2",
                ),      
                width=7,          
            )
        ]),

        # Marker style
        dbc.Row([
            dbc.Col(
                html.A("Marker style:", className="mb-2 d-block text-body text-decoration-none"),
                width=5,
            ),
            dbc.Col(
                dcc.RadioItems(
                    id=ids.RadioItems.PLOT_STYLE,
                    options=[
                       {'label': 'Pnt.', 'value': 'point'},
                       {'label': 'Ell.', 'value': 'ellipse'},
                    ],
                    inline=True,
                    className="mb-2",
                ),
                width=7,
            )
        ]),

        # Focus probes
        dbc.Row([
            dbc.Col(
                html.A("Probes:", className="mb-2 d-block text-body text-decoration-none"),
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
                    className="mb-2",
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
                className="mb-2",
            ),
        )

    ])
], className="mt-4")

