import numpy as np
from copy import copy
from io import StringIO
import os

from utils.readers import JAWFile


def mask_measurements(measurements:dict, mappattern_offset, mask_shape):

    # offset measurement using mappattern_offset to translate to instrument coordinates


    # apply masking
    

    return None


def create_masked_file(file:JAWFile, settings:dict) -> JAWFile:

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


    return out_file