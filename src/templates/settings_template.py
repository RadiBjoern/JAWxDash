import plotly.express as px


DEFAULT_SETTINGS = dict(
    # Spot settings
    marker_type="point",
    angle_of_incident=65,
    spot_size=0.3,

    # Sample settings
    colormap_value="viridis",
    colormap_options=sorted([colorscale for colorscale in px.colors.named_colorscales()]),
    sample_outline="",
    z_data_value="",

    # Mappattern offset
    x_mappattern=0.0,
    y_mappattern=2.5,
    theta_mappattern=4.1,

    # Sample offset
    x_sample=-0.067,
    y_sample=2.948,
    theta_sample=5.1,
)
