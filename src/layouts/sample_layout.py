# Package import
from dash import html, dcc, callback, Output, Input



# Local import
import ids
from utils.sample_outlines import sample_outlines
from templates.sample_template import SAMPLE_SETTINGS


sample_layout = html.Div(
    [
        dcc.Store(
            id=ids.Store.SAMPLE_SETTINGS,
            data=SAMPLE_SETTINGS,
            storage_type="memory",
        ),

        html.H6("Sample"),

        # colormaps
        html.Div(
            [
                html.H6("Colormap:", style={"marginRight": "10px"}),
                dcc.Dropdown(
                    id=ids.DropDown.COLORMAPS,
                    #options=sorted([colorscale for colorscale in px.colors.named_colorscales()]),
                    #value='viridis',
                    multi=False,
                    clearable=False,
                    style={"alignItems": "right", "width": "200px"},
                ),
            ], 
            style={"display": "flex", "alignItems": "center", "gap": "10px"}
        ),


        # sample_outline
        html.Div([
            html.H6("Outline:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id=ids.DropDown.SAMPLE_OUTLINE,
                options=list(sample_outlines.keys()),
                #value='',
                multi=False,
                clearable=True,
                style={"width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),


        # z_data
        html.Div([
            html.H6("Z-Data:", style={"marginRight": "10px"}),
            dcc.Dropdown(
                id=ids.DropDown.Z_DATA,
                options=[],
                #value='',
                multi=False,
                clearable=False,
                style={"width": "200px"},
            ),
        ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),

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
    Output(ids.DropDown.COLORMAPS, "value"),
    Output(ids.DropDown.COLORMAPS, "options"),
    Output(ids.DropDown.SAMPLE_OUTLINE, "value"),
    Output(ids.DropDown.Z_DATA, "value"),
    Input(ids.Store.SAMPLE_SETTINGS, "data"),
)
def load_default_sample_settings(sample_settings):
    return (
        sample_settings["colormap_value"],
        sample_settings["colormap_options"],
        sample_settings["outline"],
        sample_settings["z_data"],
    )