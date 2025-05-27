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
    Output(ids.Input.MAPPATTERN_X, "value"),
    Output(ids.Input.MAPPATTERN_Y, "value"),
    Output(ids.Input.MAPPATTERN_THETA, "value"),
    
    # Sample offsets
    Output(ids.Input.SAMPLE_X, "value"),
    Output(ids.Input.SAMPLE_Y, "value"),
    Output(ids.Input.SAMPLE_THETA, "value"),
    Output(ids.Input.SAMPLE_RADIUS, "value"),
    Output(ids.Input.SAMPLE_WIDTH, "value"),
    Output(ids.Input.SAMPLE_HEIGHT, "value"),
    
    # Edge exclusion
    Output(ids.RadioItems.EDGE_EXCLUSION_STATE, "value"),
    Output(ids.RadioItems.EDGE_EXCLUSION_TYPE, "value"),
    Output(ids.Input.EDGE_EXCLUSION_DISTANCE, "value"),
    Output(ids.RadioItems.BATCH_PROCESSING, "value"),

    # Input
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
        default_settings["mappattern_x"],
        default_settings["mappattern_y"],
        default_settings["mappattern_theta"],

        # Sample offset
        default_settings["sample_x"],
        default_settings["sample_y"],
        default_settings["sample_theta"],
        default_settings["sample_radius"],
        default_settings["sample_width"],
        default_settings["sample_height"],

        # Edge exclusion
        default_settings["ee_state"],
        default_settings["ee_type"],
        default_settings["ee_distance"],
        default_settings["ee_batch_processing"],
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
    Input(ids.Input.MAPPATTERN_X, "value"),
    Input(ids.Input.MAPPATTERN_Y, "value"),
    Input(ids.Input.MAPPATTERN_THETA, "value"),
    
    # Sample offset
    Input(ids.Input.SAMPLE_X, "value"),
    Input(ids.Input.SAMPLE_Y, "value"),
    Input(ids.Input.SAMPLE_THETA, "value"),
    Input(ids.Input.SAMPLE_RADIUS, "value"),
    Input(ids.Input.SAMPLE_WIDTH, "value"),
    Input(ids.Input.SAMPLE_HEIGHT, "value"),

    # Edge exclusion
    Input(ids.RadioItems.EDGE_EXCLUSION_STATE, "value"),
    Input(ids.RadioItems.EDGE_EXCLUSION_TYPE, "value"),
    Input(ids.Input.EDGE_EXCLUSION_DISTANCE, "value"),
    Input(ids.RadioItems.BATCH_PROCESSING, "value"),

    # Store state
    State(ids.Store.SETTINGS, "data"),
)
def update_offset_setting_store(
    marker_type, angle_of_incident, spot_size,
    colormap_value, sample_outline, z_data_value,
    x_map, y_map, t_map, 
    x_sam, y_sam, t_sam, r_sam, w_sam, h_sam,
    ee_state, ee_type, ee_distance, batch_processing,
    settings
    ):

    logger.debug("Updated store")

    keys = (
        "marker_type", 
        "angle_of_incident", 
        "spot_size",
        "colormap_value", 
        "sample_outline", 
        "z_data_value",
        "mappattern_x",
        "mappattern_y",
        "mappattern_theta",
        "sample_x",
        "sample_y",
        "sample_theta",
        "sample_radius",
        "sample_width",
        "sample_height",
        "ee_state", 
        "ee_type", 
        "ee_distance", 
        "batch_processing",
    )
    values = (
        marker_type, angle_of_incident, spot_size,
        colormap_value, sample_outline, z_data_value,
        x_map, y_map, t_map,
        x_sam, y_sam, t_sam, r_sam, w_sam, h_sam,
        ee_state, ee_type, ee_distance, batch_processing,
    )

    for key, value in zip(keys, values):
        settings[key] = value

    
    return settings
