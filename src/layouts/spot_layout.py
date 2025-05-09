from dash import html, dcc

import ids


spot_layout = html.Div([
    html.H6("Plotting style", style={'textAlign': 'center',}),
    dcc.RadioItems(
        id=ids.RadioItems.PLOT_STYLE,
        options=[
           {'label': 'Point', 'value': 'point'},
           {'label': 'Ellipse', 'value': 'ellipse'},
        ],
        value='point',
        inline=True,
    ),


    html.H6("Angle of incident (deg)", style={'textAlign': 'center',}),
    dcc.Slider(
        id=ids.Slider.ANGLE_OF_INCIDENT, 
        min=45, 
        max=85, 
        step=1, 
        value=65,
        marks={i: str(i) for i in range(45, 86, 5)},
    ),
    
    
    html.H6("Spot size", style={'textAlign': 'center',}),
    dcc.RadioItems(
        id=ids.RadioItems.SPOT_SIZE,
        options=[
            {'label': 'wo. FP', 'value': 0.3},
            {'label': 'w. FP', 'value': 0.03},
        ],
        value=0.3,
        inline=True,
    ),
])
