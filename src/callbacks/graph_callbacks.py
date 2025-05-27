# Library imports
from dash import callback, Output, Input, State
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import logging

# Local imports
import ids
from utils.readers import JAWFile
from utils.sample_outlines import generate_outline, radial_edge_exclusion_outline, uniform_edge_exclusion_outline
from utils.utilities import gen_spot, rotate, translate

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
    file = JAWFile.from_dict(uploaded_files[selected_file])
    


    # Setting z-data-value default if non selected
    if not settings["z_data_value"]:
        settings["z_data_value"] = sorted(file.get_z_values())[1]

    
    # exposing x,y,z data directly
    x_data = np.array(file.data["x"])
    y_data = np.array(file.data["y"])

    xy = rotate(np.vstack([x_data, y_data]), settings["mappattern_theta"])

    xy = translate(xy, [settings["mappattern_x"], settings["mappattern_y"]])
    x_data = xy[0,:]
    y_data = xy[1,:]
    
    z_data = file.data[settings["z_data_value"]].to_numpy()


    # List for holding 'shapes'
    shapes = []


    # Determine if we're plotting spots as ellipse or points
    if settings["marker_type"] == "point":
        logger.debug("Plotting 'points'")

        figure.add_trace(go.Scatter(
            x=x_data,
            y=y_data,
            mode='markers',
            marker=dict(
                size=10,
                color=z_data,  # numeric value
                colorscale=settings["colormap_value"],  # set the colormap
                colorbar=dict(title='Value'),  # optional colorbar
                showscale=True  # show the color scale
            ),
        ))


    else:
        logger.debug("Plotting NOT 'points'")

        # Making colors
        d_min, d_max = z_data.min(), z_data.max()

        norm_zdata = (z_data-d_min) / (d_max-d_min)
        colors = px.colors.sample_colorscale(colorscale=settings["colormap_value"], samplepoints=norm_zdata)
        
        shapes.extend([gen_spot(x, y, c, settings["spot_size"], settings["angle_of_incident"]) for x, y, c in zip(x_data, y_data, colors)])
    

    # Adds outline if outline is selected
    if settings["sample_outline"]:
        # add sample outline to 'shapes'
        
        shapes.append(generate_outline(settings))

    
    # Add edge exclusion outline if selected
    if settings["sample_outline"] and settings["ee_state"]:

        ee = []
        if settings["ee_type"] == "radial":
            ee.append(radial_edge_exclusion_outline(settings["sample_x"], settings["sample_y"], settings["sample_theta"], settings["ee_distance"]))
        elif settings["ee_type"] == "uniform":
            ee.append(uniform_edge_exclusion_outline(settings["sample_x"], settings["sample_y"], settings["sample_theta"], settings["ee_distance"]))

        shapes.extend(ee)
    

    # Calculate 'zoom-window'
    xmin, xmax = min(x_data), max(x_data)
    ymin, ymax = min(y_data), max(y_data)
    scale_factor = 0.2
    scale_range = xmax - xmin

    #Adding shapes to the figure
    figure.update_layout(
        shapes=shapes,
        xaxis=dict(range=[xmin - scale_factor*scale_range, xmax + scale_factor*scale_range]),
        yaxis=dict(range=[ymin - scale_factor*scale_range, ymax + scale_factor*scale_range]),
    )


    return figure, sorted(file.get_z_values())
