from dash import dcc, html


import ids


stage_layout = html.Div([
    html.Div([
        html.H6("Stage outline", style={"marginRight": "10px"}),
        dcc.RadioItems(
            id=ids.RadioItems.STAGE_STATE,
            options=[
                {"label": "ON", "value": True},
                {"label": "OFF", "value": False},
            ],
            inline=True,
            style={"alighItems": "right", "width": "200px"},
        )
    ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),
],
style={
        'width': '100%',
        #'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'solid',
        'borderRadius': '10px',
        'textAlign': 'center',
        'margin': '10px'
    },
)