import numpy as np
from numpy import pi, sin, cos
import plotly.graph_objects as go

def degree2rad(degrees):
    return degrees*pi/180

def disk_part(center=[0,0], radius=1, start_angle=0, end_angle=90, n=50, seg=True):
    sta = degree2rad(start_angle)
    ea = degree2rad(end_angle)
    t = np.linspace(sta, ea, n)
    x = center[0] + radius*cos(t)
    y = center[1] +radius*sin(t)
    path = f"M {x[0]},{y[0]}"

    for xc, yc in zip(x[1:], y[1:]):
        path += f" L{xc},{yc}"

    if seg: #segment
        return path + " Z"
    
    else: #disk sector
        return path + f" L{center[0]},{center[1]} Z" #sector 

path_sect = disk_part(center=[1, 0], radius=1.5, start_angle=30, end_angle=120, seg=False)
#path_segment = disk_part(center=[1,0], radius=1.75, start_angle=190, end_angle=280)

fig = go.Figure()
fig.update_layout(width=700, height=500,
                  xaxis_range=[0,2], yaxis_range=[-2, 2],
                  shapes=[dict(type="path",
                               path=path_sect,
                               fillcolor="LightPink",
                               line_color="Crimson"),
#                          dict(type="path",
#                               path=path_segment,
#                               fillcolor="LightPink",
#                               line_color="Crimson") 
                         ])
fig.update_yaxes(scaleanchor = "x", #IMPORTANT These yaxis settings ensure that the circle is non-deformed
                 scaleratio = 1)


fig.show()
