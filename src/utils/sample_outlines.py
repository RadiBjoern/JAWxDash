import numpy as np


from utils.utilities import rotate, translate

INCH2MM = 25.4
INCH2CM = 2.54


def generate_outline(settings:dict) -> dict:

    if settings["sample_outline"] == "circle":
        return dict(
            type="circle",
            x0=settings["sample_x"] - settings["sample_radius"],
            x1=settings["sample_x"] + settings["sample_radius"],
            y0=settings["sample_y"] - settings["sample_radius"],
            y1=settings["sample_y"] + settings["sample_radius"],
            line_color="RoyalBlue",
        )
    

    elif settings["sample_outline"] == "rectangle_corner":
        #x, y = settings["sample_x"], settings["sample_y"]
        w, h = settings["sample_width"], settings["sample_height"]

        x = (0, w, w, 0, 0)
        y = (0, 0, h, h, 0)
        xy = np.asarray([x,y])
        
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
            line_color="RoyalBlue",
        )


    elif settings["sample_outline"] == "sector":

        t1 = np.deg2rad(settings["sample_theta"])
        t2 = t1 + 0.5*np.pi

        t = np.linspace(t1, t2, 50)
        x = settings["sample_x"] + settings["sample_radius"] * np.cos(t)
        y = settings["sample_y"] + settings["sample_radius"] * np.sin(t)

        path = f"M {settings["sample_x"]},{settings["sample_y"]}"

        for xc, yc in zip(x, y):
            path += f" L{xc},{yc}"

        path += f" L{settings["sample_x"]},{settings["sample_y"]} Z"

        return dict(
            type="path",
            path=path,
            line_color="RoyalBlue",
        )


    else:
        return dict()



sample_outlines = [
    {"label": "Circle", "value": "circle"},
    {"label": "Rectangle (center)", "value": "rectangle_center"},
    {"label": "Rectangle (corner)", "value": "rectangle_corner"},
    {"label": "Sector", "value": "sector"},
]



def radial_edge_exclusion_outline(x_sample, y_sample, t_off, ee_dist):
    t1 = np.deg2rad(0 + t_off)
    t2 = np.deg2rad(90 + t_off)


    # Creating arc
    t = np.linspace(t1, t2, 50)
    x = x_sample + (2*2.54-ee_dist) * np.cos(t)
    y = y_sample + (2*2.54-ee_dist) * np.sin(t)
    path = f"M {x[0]},{y[0]}"
    for xc, yc in zip(x[1:], y[1:]):
        path += f" L{xc},{yc}"


    shapes=[
        dict(
            type="line",
            x0=x_sample,
            y0=y_sample,
            x1=(2*2.54-ee_dist) * np.cos(t1) + x_sample,
            y1=(2*2.54-ee_dist) * np.sin(t1) + y_sample,
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        ),
        dict(
            type="line",
            x0=x_sample,
            y0=y_sample,
            x1=(2*2.54-ee_dist) * np.cos(t2) + x_sample,
            y1=(2*2.54-ee_dist) * np.sin(t2) + y_sample,
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        ),
        dict(
            type="path",
            path=path, #sector
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        ),
    ]

    return shapes



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

    # Calc edge lengths
    e_ee = np.sqrt((2*2.54-ee_dist)**2 - ee_dist**2) - ee_dist

    # Calc offset angle 
    t_o = np.arcsin(ee_dist/(2*2.54-ee_dist))
    

    # Creating arc
    t = np.linspace(t1+t_o, t2-t_o, 50)
    x = x_sample + (2*2.54-ee_dist) * np.cos(t)
    y = y_sample + (2*2.54-ee_dist) * np.sin(t)
    path = f"M {x[0]},{y[0]}"
    for xc, yc in zip(x[1:], y[1:]):
        path += f" L{xc},{yc}"


    shapes=[
        dict(
            type="line",
            x0=x_ee,
            y0=y_ee,
            x1=e_ee * np.cos(t1) + x_ee,
            y1=e_ee * np.sin(t1) + y_ee,
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        ),
        dict(
            type="line",
            x0=x_ee,
            y0=y_ee,
            x1=e_ee * np.cos(t2) + x_ee,
            y1=e_ee * np.sin(t2) + y_ee,
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        ),
        dict(
            type="path",
            path=path, #sector
            line=dict(color="rgba(193, 0, 1, 255)", width=2),
        ),
    ]
    return shapes
    


