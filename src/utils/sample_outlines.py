import numpy as np


INCH2MM = 25.4
INCH2CM = 2.54


def wafer_inch(dia_inch:float) -> dict:
    
    def wafer_inch_offset(x_off=0, y_off=0, t_off=0):
        r_inch = 0.5 * dia_inch
        return dict(
            type='circle',
            x0=-r_inch*INCH2CM+x_off,
            y0=-r_inch*INCH2CM+y_off,
            x1=r_inch*INCH2CM+x_off,
            y1=r_inch*INCH2CM+y_off,
            line=dict(
                color="rgba(1, 0, 0, 1)",
                width=1,
                dash='solid',
            ),
            fillcolor="rgba(0, 0, 0, 0)",
            name="sample_outline",
        )
    
    return wafer_inch_offset


def quarter_wafer_inch(dia_inch:float) -> dict:

    def quarter_wafer_inch_offset(x_off:float=0, y_off:float=0, t_off:float=0):
    
        radius_cm = .5 * dia_inch * 2.54
        center = (x_off, y_off)

        n = 50
        t1_deg = 0 + t_off
        t2_deg = 90 + t_off
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
    
    return quarter_wafer_inch_offset
    


sample_outlines = {
    "wafer 4 inch": wafer_inch(4),
    "wafer 6 inch": wafer_inch(6),
    "wafer 8 inch": wafer_inch(8),
    "1/4 wafer 4 inch": quarter_wafer_inch(4),
}
