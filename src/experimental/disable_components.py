import dash
from dash import dcc, html, Input, Output, State

app = dash.Dash(__name__)

# Helper to generate radio options with optional disabling
def get_radio_options(disabled=False):
    return [
        {"label": "Choice A", "value": "A", "disabled": disabled},
        {"label": "Choice B", "value": "B", "disabled": disabled}
    ]

app.layout = html.Div([
    html.H4("Control Panel"),
    
    # Master control to enable/disable inputs
    dcc.Dropdown(
        id='enable-toggle',
        options=[
            {'label': 'Enable All Inputs', 'value': 'enable'},
            {'label': 'Disable All Inputs', 'value': 'disable'}
        ],
        value='enable',
        style={'width': '300px'}
    ),

    html.Br(),

    html.Div([
        html.H6("Text Input:"),
        dcc.Input(id='my-input', type='text', value='Type here...', debounce=True)
    ]),

    html.Br(),

    html.Div([
        html.H6("Dropdown:"),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Option 1', 'value': 'opt1'},
                {'label': 'Option 2', 'value': 'opt2'}
            ],
            value='opt1'
        )
    ]),

    html.Br(),

    html.Div([
        html.H6("Radio Items:"),
        dcc.RadioItems(
            id='my-radio',
            options=get_radio_options(False),
            value='A'
        )
    ])
])

# Callback to enable/disable all inputs
@app.callback(
    Output('my-input', 'disabled'),
    Output('my-dropdown', 'disabled'),
    Output('my-radio', 'options'),
    Input('enable-toggle', 'value')
)
def toggle_all_inputs(mode):
    disable = (mode == 'disable')
    return disable, disable, get_radio_options(disable)

if __name__ == '__main__':
    app.run_server(debug=True)
