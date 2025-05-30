import ezdxf
import numpy as np


def arc_to_path(center, radius, t1_deg, t2_deg, closed=False):
    """
    Generates an arc consisting of line segments
    
    Returns: dict
    """
    
    n = int((t2_deg - t1_deg) / 5 + 1)
    t = np.deg2rad(np.linspace(t1_deg, t2_deg, n))
    x = center[0] + radius*np.cos(t)
    y = center[1] + radius*np.sin(t)

    path = f"M {x[0]}, {y[0]}"
    for xc, yc in zip(x,y):
        path += f"L {xc},{yc}"
    
    if closed:
        path += " Z"

    return dict(
        type="path",
        path=path,
        line={"color": "rgba(0.5, 0.5, 0.5, 0.35)", "width": 1}
    )


def circle_to_path(center, radius):
    """
    Generates a circle path
    
    Return: dict
    """
    
    return dict(
        type="circle",
        xref="x",
        yref="y",
        x0=center[0] - radius,
        y0=center[1] - radius,
        x1=center[0] + radius,
        y1=center[1] + radius,
        line={"color": "rgba(0.5, 0.5, 0.5, 0.35)", "width": 1}
    )


def line_to_path(xy_start, xy_end):
    """
    Generates a line path
    
    Returns: dict
    """
    
    return dict(
        type="line",
        x0=xy_start[0],
        y0=xy_start[1],
        x1=xy_end[0],
        y1=xy_end[1],
        line={"color": "rgba(0.5, 0.5, 0.5, 0.35)", "width": 1}
    )


def dxf_to_path(file_path:str) -> list[dict]:


    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    shapes = []

    # Loop through entities and create shapes
    for entity in msp:
        dxftype = entity.dxftype()

        if dxftype == "ARC":
            center = entity.dxf.center
            radius = entity.dxf.radius
            t1 = entity.dxf.start_angle
            t2 = entity.dxf.end_angle

            shapes.append(arc_to_path(center, radius, t1, t2))
        
        elif dxftype == "CIRCLE":
            center = entity.dxf.center
            radius = entity.dxf.radius
            
            shapes.append(circle_to_path(center, radius))
        

        elif dxftype == "LINE":
            start = entity.dxf.start
            end = entity.dxf.end

            shapes.append(line_to_path(start, end))
    

    return shapes