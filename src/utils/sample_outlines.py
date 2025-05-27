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
    {"label": "Rectangle (corner)", "value": "rectangle_corner"},
    {"label": "Sector", "value": "sector"},
]

