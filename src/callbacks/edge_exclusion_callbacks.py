from dash import callback, dcc, Input, Output, State
import numpy as np
import logging
from copy import copy
from io import StringIO

from utils.readers import JAWFile
import ids


logger = logging.getLogger(__name__)


@callback(
    Output(ids.Download.EDGE_EXCLUDED_FILE, "data"),
    Input(ids.Button.DOWNLOAD_MASKED_DATA, "n_clicks"),
    State(ids.DropDown.UPLOADED_FILES, "value"),
    State(ids.Store.UPLOADED_FILES, "data"),
    State(ids.Store.SETTINGS, "data"),
)
def download_edge_exclusion(n_clicks, selected_file:str, stored_files:dict, settings:dict):
    
    logger.debug("Button pressed")

    # check if a file is selected and edge exclusion is turned on
    if not selected_file or not settings["ee_state"]:
        return None


    file = JAWFile.from_dict(stored_files[selected_file])

    # Getting instrumented coordinate of the measurement
    xy_off = file.offset(
        x=settings["x_mappattern"],
        y=settings["y_mappattern"],
        theta=settings["theta_mappattern"],
    )

    

    if settings["ee_type"] == "radial":

        # Sector parameters
        cx, cy = settings["x_sample"], settings["y_sample"]  # center
        radius = (2*2.54 - settings["ee_distance"])
        angle_start = np.deg2rad(0 + settings["theta_sample"])  # in radians
        angle_end = np.deg2rad(90 + settings["theta_sample"])


        # Polar coordinates
        dx = xy_off[:,0] - cx
        dy = xy_off[:,1] - cy
        r = np.sqrt(dx**2 + dy**2)
        theta = np.arctan2(dy, dx)


        # Normalize angle to [0, 2pi]
        theta = (theta + 2 * np.pi) % (2 * np.pi)

        mask = (r <= radius) & (theta >= angle_start) & (theta <= angle_end)


    else:
        print("Edge exclusion type not implemented. Please select another")


    out_file = copy(file)
    out_file.data = file.data[mask]


    out_file.data.drop(["x", "y"], axis="columns", inplace=True)


    # Check the new header
    out_file.update_header()

    # Build the output manually
    buffer = StringIO()

    # 1. Write header
    for line in out_file.header:
        buffer.write(line)

    # 2. Write data rows
    for row in out_file.data.itertuples(index=False):
        buffer.write("\t".join(map(str, row)) + "\n")
    
    buffer.seek(0)

    return dcc.send_string(buffer.getvalue(), filename="output.txt")