from dash import dcc, html
import dash_bootstrap_components as dbc
import logging

import ids


logger = logging.getLogger(__name__)


spot_layout = dbc.Card([
    dbc.CardHeader("Beam Settings"),
    dbc.CardBody([
        dbc.Row([
            # Left column w. text
            dbc.Col([
                html.A("Z-Data:", className="mb-3 d-block text-body text-decoration-none"),
                html.A("Colormap:", className="mb-3 d-block text-body text-decoration-none"),
                html.A("Marker style:", className="mb-3 d-block text-body text-decoration-none"),
                html.A("Focus probes:", className="mb-3 d-block text-body text-decoration-none"),
            ], width=5, style={'display': 'flex', 'flexDirection': 'column', 'gap': '0.9rem'}),


            # Right column w. dropdown
            dbc.Col([
                dcc.Dropdown(
                    id=ids.DropDown.Z_DATA,
                    options=[],
                    multi=False,
                    clearable=False,
                    className="mb-3",
                ),

                dcc.Dropdown(
                    id=ids.DropDown.COLORMAPS,
                    multi=False,
                    clearable=False,
                    className="mb-3",
                ),

                dcc.RadioItems(
                    id=ids.RadioItems.PLOT_STYLE,
                    options=[
                       {'label': 'Pnt.', 'value': 'point'},
                       {'label': 'Ell.', 'value': 'ellipse'},
                    ],
                    inline=True,
                    className="mb-3",
                ),

                dcc.RadioItems(
                    id=ids.RadioItems.SPOT_SIZE,
                    options=[
                        {'label': 'ON', 'value': 0.03},
                        {'label': 'OFF', 'value': 0.3},
                    ],
                    inline=True,
                    className="mb-3",
                ),
            ], width=7),
        ], className="gy-2"),


        # Angle of incident
        html.H6("Angle of incident (deg)", style={'textAlign': 'center',}),
        dcc.Slider(
            id=ids.Slider.ANGLE_OF_INCIDENT, 
            min=45, 
            max=85, 
            step=1, 
            marks={i: str(i) for i in range(45, 86, 5)},
            className="mb-3",
        ),
    ])
], className="mt-4")

