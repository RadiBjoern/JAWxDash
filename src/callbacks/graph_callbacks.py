# Library imports
from dash import callback, Output, Input, State
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import logging

# Local imports
import ids
from utils.utilities import gen_spot
from utils.sample_outlines import sample_outlines

from templates.graph_template import FIGURE_LAYOUT

logger = logging.getLogger(__name__)


CRITICAL_COUNT = 500


# Adding a placeholder for sample outline
# 8in wafer
r = 1*2.54

@callback(
        Output(ids.Graph.MAIN, "figure"),
        Output(ids.DropDown.Z_DATA, "options"),
        Input(ids.DropDown.UPLOADED_FILES, "value"),
        State(ids.Store.UPLOADED_FILES, "data"),
        Input(ids.Store.SETTINGS, "data")
)
def update_figure(
    selected_file:str, 
    uploaded_files:dict, 
    settings:dict
    ) -> go.Figure:
    """
    Updates the figure, in accordance with:
    - Selected file
    - Spot style
        - Shape [point/ellipse]
        - Size [focus probe on/off]
        - Angle of incident
        - Colormap
    - Sample outline
    - Data 'channel'
    - MapPattern offset
        - x
        - y
        - theta
    - Sample offset
        - x
        - y
        - theta
    """
    
    logger.debug("Tiggered")

    # Setting up an empty figure
    figure = go.Figure(
        layout=go.Layout(
            FIGURE_LAYOUT  # Joining the template with the updates
        ),
    )
    

    # If no file or z-data-value selected, return an empty figure
    if not selected_file:
        return figure, []
    
    
    
    # A sample has been selected, now let's unpack
    sample = uploaded_files[selected_file]
    data = sample["data"]


    # Setting z-data-value default if non selected
    if not settings["z_data_value"]:
        settings["z_data_value"] = sorted(list(data.keys()))[0]

    z_data = np.array(data[settings["z_data_value"]])


    # List for holding 'shapes'
    shapes = []


    # Determine if we're plotting spots as ellipse or points
    if settings["marker_type"] == "point":
        logger.debug("Plotting 'points'")

        figure.add_trace(go.Scatter(
            x=data["x"],
            y=data["y"],
            mode='markers',
            marker_color=z_data,
        ))


    else:
        logger.debug("Plotting NOT 'points'")

        # Making colors
        d_min, d_max = min(z_data), max(z_data)

        norm_zdata = (z_data-d_min) / (d_max-d_min)
        colors = px.colors.sample_colorscale(colorscale=settings["colormap_value"], samplepoints=norm_zdata)
        
        shapes.extend([gen_spot(x, y, c, settings["spot_size"], settings["angle_of_incident"]) for x, y, c in zip(data["x"], data["y"], colors)])
    

    # Adds outline if outline is selected
    if settings["sample_outline"]:
        # add sample outline to 'shapes'
        kwargs = dict(
            x_off = settings["x_sample"], 
            y_off = settings["y_sample"],
            t_off = settings["theta_sample"],
        )
        
 
        shapes.append(sample_outlines[settings["sample_outline"]](**kwargs))


    # Calculate 'zoom-window'
    xmin, xmax = min(data["x"]), max(data["x"])
    ymin, ymax = min(data["y"]), max(data["y"])


    #Adding shapes to the figure
    figure.update_layout(
        shapes=shapes,
        xaxis=dict(range=[xmin, xmax]),
        yaxis=dict(range=[ymin, ymax]),
    )


    return figure, sorted(list(data.keys()))
