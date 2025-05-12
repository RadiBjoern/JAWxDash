import numpy as np


INCH2MM = 25.4
INCH2CM = 2.54


def wafer_inch(dia_inch:float) -> dict:
    r_inch = 0.5 * dia_inch
    return dict(
        type='circle',
        x0=-r_inch*INCH2CM,
        y0=-r_inch*INCH2CM,
        x1=r_inch*INCH2CM,
        y1=r_inch*INCH2CM,
        line=dict(
            color="rgba(1, 0, 0, 1)",
            width=1,
            dash='solid',
        ),
        fillcolor="rgba(0, 0, 0, 0)",
        name="sample_outline",
    )

def quarter_wafer_inch(dia_inch:float) -> dict:

    radius_cm = .5 * dia_inch * 2.54
    center = (-0.0673, 0.822)
    n = 50
    t1_deg = 225 + 1
    t2_deg = 315 + 1
    t1_rad = np.deg2rad(t1_deg)
    t2_rad = np.deg2rad(t2_deg)

    t = np.linspace(t1_rad, t2_rad, n)
    x = center[0] + radius_cm * np.cos(t)
    y = center[1] + radius_cm * np.sin(t)

    path = f"M {x[0]},{y[0]}"

    for xc, yc in zip(x[1:], y[1:]):
        path += f" L{xc},{yc}"

    
    return dict(
        type="path",
        path=path + f" L{center[0]},{center[1]} Z", #sector
        line_color="Crimson",
    )
    


sample_outlines = {
    "wafer 4 inch": wafer_inch(4),
    "wafer 6 inch": wafer_inch(6),
    "wafer 8 inch": wafer_inch(8),
    "1/4 wafer 4 inch": quarter_wafer_inch(4),
}
