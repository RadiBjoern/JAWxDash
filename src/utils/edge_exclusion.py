import numpy as np
from copy import copy


from utils.readers import JAWFile



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



def radial_edge_exclusion_outline(x_sample, y_sample, t_off, ee_dist):
    t1 = np.deg2rad(0 + t_off)
    t2 = np.deg2rad(90 + t_off)


    # Creating arc
    t = np.linspace(t1, t2, 50)
    x = x_sample + (2*2.54-ee_dist) * np.cos(t)
    y = y_sample + (2*2.54-ee_dist) * np.sin(t)


    path = f"M {x_sample},{y_sample}"
    for xc, yc in zip(x, y):
        path += f" L{xc},{yc}"

    path += f" L{x_sample},{y_sample} Z"


    return dict(
        type="path",
        path=path, #sector
        line=dict(color="rgba(193, 0, 1, 255)", width=2),
    )



def uniform_edge_exclusion_outline(x_sample, y_sample, t_off, ee_dist):

    # Calculate 'intermitten' angle
    t1 = np.deg2rad(0 + t_off)
    t2 = np.deg2rad(90 + t_off)
    t_ee = (t2-t1)/2 + t1

    # Calculate 'intermitten' length
    c = ee_dist/np.cos(np.pi/4)

    # Calculate 90deg corner of shrunken sector
    x_ee = np.cos(t_ee) * c + x_sample
    y_ee = np.sin(t_ee) * c + y_sample

    # Calc offset angle 
    t_o = np.arcsin(ee_dist/(2*2.54-ee_dist))
    

    # Creating arc
    t = np.linspace(t1+t_o, t2-t_o, 50)
    x = x_sample + (2*2.54-ee_dist) * np.cos(t)
    y = y_sample + (2*2.54-ee_dist) * np.sin(t)

    path = f"M {x_ee},{y_ee}"
    for xc, yc in zip(x, y):
        path += f" L{xc},{yc}"

    path += f" L{x_ee},{y_ee} Z"


    return dict(
        type="path",
        path=path, #sector
        line=dict(color="rgba(193, 0, 1, 255)", width=2),
    )

