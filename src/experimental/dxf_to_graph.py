import ezdxf
import numpy as np
import plotly.graph_objects as go
import os


print(os.getcwd())

# Load your DXF file
doc = ezdxf.readfile("src/assets/JAW stage outline.dxf")
msp = doc.modelspace()

# Initialize list of shapes
shapes = []

def arc_to_path(center, radius, start_angle, end_angle, closed= False):

    t = np.deg2rad(np.linspace(start_angle, end_angle, 50))
    x = center[0] + radius*np.cos(t)
    y = center[1] + radius*np.sin(t)

    path = f'M {x[0]}, {y[0]}'
    for k in range(1, len(t)):
        path += f'L{x[k]}, {y[k]}'
    if closed:
        path += ' Z'
    return path 



# Loop through entities and create shapes
n_arc = 0
for entity in msp:
    if entity.dxftype() == "ARC":
        n_arc += 1
        center = entity.dxf.center
        radius = entity.dxf.radius
        start_angle = entity.dxf.start_angle
        end_angle = entity.dxf.end_angle

        path = arc_to_path((center.x, center.y), radius, start_angle, end_angle)
        shapes.append({
            'type': 'path',
            'path': path,
            'line': {'color': 'rgba(0.5, 0.5, 0.5, 0.35)', "width": 1}
        })

    elif entity.dxftype() == "CIRCLE":
        center = entity.dxf.center
        radius = entity.dxf.radius
        shapes.append({
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': center[0] - radius, 'y0': center[1] - radius,
            'x1': center[0] + radius, 'y1': center[1] + radius,
            'line': {'color': 'rgba(0.5, 0.5, 0.5, 0.35)', "width": 1}
        })

    elif entity.dxftype() == "LINE":
        start = entity.dxf.start
        end = entity.dxf.end
        shapes.append({
            'type': 'line',
            'x0': start[0], 'y0': start[1],
            'x1': end[0], 'y1': end[1],
            'line': {'color': 'rgba(0.5, 0.5, 0.5, 0.35)', "width": 1}
        })

print("no. arc: %i" % n_arc)


# Create figure
fig = go.Figure()
fig.update_layout(
    shapes=shapes,
    xaxis=dict(scaleanchor="y", showgrid=False),
    yaxis=dict(showgrid=False),
    plot_bgcolor='white'
)

fig.show()
