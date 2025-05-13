from dash import dcc, html, callback, Output, Input
import logging

import ids
from templates.spot_template import SPOT_DEFAULT_SETTINGS


logger = logging.getLogger(__name__)


spot_layout = html.Div(
    [
        dcc.Store(
            id=ids.Store.SPOT_SETTINGS,
            data=SPOT_DEFAULT_SETTINGS,
            storage_type="memory",
        ),

        html.Div([
            html.H6("Marker style:", style={"marginRight": "10px"}),
            dcc.RadioItems(
                id=ids.RadioItems.PLOT_STYLE,
                options=[
                   {'label': 'Point', 'value': 'point'},
                   {'label': 'Ellipse', 'value': 'ellipse'},
                ],
                #value='point',
                inline=True,
                style={"alignItems": "right", "width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),

    
        html.H6("Angle of incident (deg)", style={'textAlign': 'center',}),
        dcc.Slider(
            id=ids.Slider.ANGLE_OF_INCIDENT, 
            min=45, 
            max=85, 
            step=1, 
            #value=65,
            marks={i: str(i) for i in range(45, 86, 5)},
        ),


        html.Div([
            html.H6("Spot size", style={"marginRight": "10px"}),
            dcc.RadioItems(
                id=ids.RadioItems.SPOT_SIZE,
                options=[
                    {'label': 'wo. FP', 'value': 0.3},
                    {'label': 'w. FP', 'value': 0.03},
                ],
                #value=0.3,
                inline=True,
                style={"alignItems": "right", "width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"})
    ]
)


@callback(
    Output(ids.RadioItems.PLOT_STYLE, "value"),
    Output(ids.Slider.ANGLE_OF_INCIDENT, "value"),
    Output(ids.RadioItems.SPOT_SIZE, "value"),
    Input(ids.Store.SPOT_SETTINGS, "data"),
    prevent_initial_call=False,
)
def load_defaults_spot_settings(data):
    """
    RadioItems -> value='point'
    Slider -> value=65
    RadioItems -> value=0.3
    """
    return (
        data["marker_type"],
        data["angle_of_incident"],
        data["spot_size"],
    )


@callback(
    Output(ids.Store.SPOT_SETTINGS, "data"),
    Input(ids.RadioItems.PLOT_STYLE, "value"),
    Input(ids.Slider.ANGLE_OF_INCIDENT, "value"),
    Input(ids.RadioItems.SPOT_SIZE, "value"),
    prevent_initial_call=True,
)
def update_spot_settings_store(marker_type, angle_of_incident, spot_size):
    logger.debug("Ran")

    return dict(
        marker_type=marker_type,
        angle_of_incident=angle_of_incident,
        spot_size=spot_size,
    )