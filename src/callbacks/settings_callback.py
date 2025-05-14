from dash import callback, Output, Input, State
import logging


import ids

logger = logging.getLogger(__name__)


@callback(
    # Spot
    Output(ids.RadioItems.PLOT_STYLE, "value"),
    Output(ids.Slider.ANGLE_OF_INCIDENT, "value"),
    Output(ids.RadioItems.SPOT_SIZE, "value"),
    # Sample
    Output(ids.DropDown.COLORMAPS, "value"),
    Output(ids.DropDown.COLORMAPS, "options"),
    Output(ids.DropDown.SAMPLE_OUTLINE, "value"),
    Output(ids.DropDown.Z_DATA, "value"),
    # MapPattern offsets
    Output(ids.Offset.MAPPATTERN_X, "value"),
    Output(ids.Offset.MAPPATTERN_Y, "value"),
    Output(ids.Offset.MAPPATTERN_THETA, "value"),
    # Sample offsets
    Output(ids.Offset.SAMPLE_X, "value"),
    Output(ids.Offset.SAMPLE_Y, "value"),
    Output(ids.Offset.SAMPLE_THETA, "value"),
    Input(ids.Store.DEFAULT_SETTINGS, "data"),
)
def load_default_settings(default_settings):

    logger.debug("Loaded settings")

    return (
        # Spot
        default_settings["marker_type"],
        default_settings["angle_of_incident"],
        default_settings["spot_size"],
        
        # Sample
        default_settings["colormap_value"],
        default_settings["colormap_options"],
        default_settings["sample_outline"],
        default_settings["z_data_value"],
        
        # Mappattern offset
        default_settings["x_mappattern"],
        default_settings["y_mappattern"],
        default_settings["theta_mappattern"],

        # Sample offset
        default_settings["x_sample"],
        default_settings["y_sample"],
        default_settings["theta_sample"],
    )


@callback(
    Output(ids.Store.SETTINGS, "data"),
    
    # Spot
    Input(ids.RadioItems.PLOT_STYLE, "value"),
    Input(ids.Slider.ANGLE_OF_INCIDENT, "value"),
    Input(ids.RadioItems.SPOT_SIZE, "value"),

    # Sample
    Input(ids.DropDown.COLORMAPS, "value"),
    Input(ids.DropDown.SAMPLE_OUTLINE, "value"),
    Input(ids.DropDown.Z_DATA, "value"),
    
    # MapPattern offset
    Input(ids.Offset.MAPPATTERN_X, "value"),
    Input(ids.Offset.MAPPATTERN_Y, "value"),
    Input(ids.Offset.MAPPATTERN_THETA, "value"),
    
    # Sample offset
    Input(ids.Offset.SAMPLE_X, "value"),
    Input(ids.Offset.SAMPLE_Y, "value"),
    Input(ids.Offset.SAMPLE_THETA, "value"),

    # Store state
    State(ids.Store.SETTINGS, "data"),
)
def update_offset_setting_store(
    marker_type, angle_of_incident, spot_size,
    colormap_value, sample_outline, z_data_value,
    x_map, y_map, t_map, 
    x_sam, y_sam, t_sam, 
    settings
    ):

    logger.debug("Updated store")

    keys = (
        "marker_type", "angle_of_incident", "spot_size",
        "colormap_value", "sample_outline", "z_data_value",
        "x_mappattern", "y_mappattern", "theta_mappattern",
        "x_sample", "y_sample", "theta_sample",
    )
    values = (
        marker_type, angle_of_incident, spot_size,
        colormap_value, sample_outline, z_data_value,
        x_map, y_map, t_map,
        x_sam, y_sam, t_sam,
    )

    for key, value in zip(keys, values):
        settings[key] = value

    
    return settings
