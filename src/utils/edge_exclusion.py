import numpy as np
from copy import copy
import logging

from utils.readers import JAWFile
from utils.utilities import rotate, translate


logger = logging.getLogger(__name__)


def create_masked_file(file:JAWFile, settings:dict) -> JAWFile:


    # Getting instrumented coordinate of the measurement
    xy_off = file.offset(
        x=settings["mappattern_x"],
        y=settings["mappattern_y"],
        theta=settings["mappattern_theta"],
    )

    

    if settings["ee_type"] == "radial":

        # Sector parameters
        cx, cy = settings["sample_x"], settings["sample_y"]  # center
        radius = (settings["sample_radius"] - settings["ee_distance"])
        angle_start = np.deg2rad(0 + settings["sample_theta"])  # in radians
        angle_end = np.deg2rad(90 + settings["sample_theta"])


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


    out_file.data = out_file.data.drop(["x", "y"], axis="columns")


    # Check the new header
    out_file.update_header()


    return out_file



def _circle_edge_exclusion_(x, y, radius, ee_distance) -> dict:
    
    return dict(
            type="circle",
            x0=x - radius + ee_distance,
            y0=y - radius + ee_distance,
            x1=x + radius - ee_distance,
            y1=y + radius - ee_distance,
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        )



def radial_edge_exclusion_outline(settings):

    x, y = settings["sample_x"], settings["sample_y"]
    d = settings["ee_distance"]
    r =  settings["sample_radius"]


    # Circle outline
    if settings["sample_outline"] == "circle":

        return _circle_edge_exclusion_(x, y, r, d)
    

    # Rectangle (corner) outline
    elif settings["sample_outline"] == "rectangle_corner":
        logger.warning("Rectangle (corner) radial edge exclusion method not implemented")

        return dict()
    

    # Sector outline
    elif settings["sample_outline"] == "sector":
        
        t = settings["sample_theta"]

        t1 = np.deg2rad(t)
        t2 = t1 + 0.5*np.pi


        # Creating arc
        t = np.linspace(t1, t2, 50)
        x_arc = x + (r-d) * np.cos(t)
        y_arc = y + (r-d) * np.sin(t)


        path = f"M {x},{y}"
        for xc, yc in zip(x_arc, y_arc):
            path += f" L{xc},{yc}"

        path += f" L{x},{y} Z"

        
        return dict(
            type="path",
            path=path, #sector
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        )
    

    else:
        return dict()



def uniform_edge_exclusion_outline(settings):

    x, y = settings["sample_x"],  settings["sample_y"]
    d = settings["ee_distance"]

    # Circle outline
    if settings["sample_outline"] == "circle":
        r =  settings["sample_radius"]

        return _circle_edge_exclusion_(x, y, r, d)
    

    # Rectangle (corner) outline
    elif settings["sample_outline"] == "rectangle_corner":
        x, y = settings["sample_x"], settings["sample_y"]
        w, h = settings["sample_width"], settings["sample_height"]
        d = settings["ee_distance"]

        xc = (0+d, w-d, w-d, 0+d, 0+d)
        yc = (0+d, 0+d, h-d, h-d, 0+d)
        xy = np.asarray([xc, yc])

        # Rotate and translate
        xy_rot = rotate(xy, settings["sample_theta"])
        xy_rot_tran = translate(xy_rot, np.asarray([settings["sample_x"], settings["sample_y"]]))

        x = xy_rot_tran[0,:]
        y = xy_rot_tran[1,:]

        path = f"M {x[0]},{y[0]}"

        for xc, yc in zip(x[1:-1], y[1:-1]):
            path += f" L{xc},{yc}"

        path += f" L{x[-1]},{y[-1]} Z"

        return dict(
            type="path",
            path=path,
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        )
    
    
    # Sector outline
    elif settings["sample_outline"] == "sector":
        theta = settings["sample_theta"]
        r = settings["sample_radius"]
        
        t1 = np.deg2rad(theta)
        t2 = t1 + 0.5*np.pi

        # Calculate 'intermitten' angle
        t_ee = (t2-t1)/2 + t1

        # Calculate 'intermitten' length
        c = d/np.cos(np.pi/4)

        # Calculate 90deg corner of shrunken sector
        x_ee = np.cos(t_ee) * c + x
        y_ee = np.sin(t_ee) * c + y

        # Calc offset angle 
        t_o = np.arcsin(d/(r-d))


        # Creating arc
        t = np.linspace(t1+t_o, t2-t_o, 50)
        x_arc = x + (r-d) * np.cos(t)
        y_arc = y + (r-d) * np.sin(t)

        path = f"M {x_ee},{y_ee}"
        for xc, yc in zip(x_arc, y_arc):
            path += f" L{xc},{yc}"

        path += f" L{x_ee},{y_ee} Z"


        return dict(
            type="path",
            path=path, #sector
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        )
    
    else:
        return dict()

