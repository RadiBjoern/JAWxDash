from dash import html


from spot import angle_of_incident, plot_style, spot_size


spot_settings = html.Div([
    html.H6("Plotting style", style={'textAlign': 'center',}),
    plot_style,
    html.H6("Angle of incident (deg)", style={'textAlign': 'center',}),
    angle_of_incident,
    html.H6("Spot size", style={'textAlign': 'center',}),
    spot_size,
])
