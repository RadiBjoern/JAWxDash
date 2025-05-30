import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample inputs for grid
input_grid = [
    dcc.Input(id=f"input-{i}", placeholder=f"Input {i+1}", type="text", style={"width": "100%"})
    for i in range(6)
]

app.layout = dbc.Container([
    dbc.Row([
        # Column 1
        dbc.Col([
            html.H5("Controls"),
            dcc.Upload(
                id='upload-data',
                children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'marginBottom': '10px'
                }
            ),
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Option A', 'value': 'A'},
                    {'label': 'Option B', 'value': 'B'}
                ],
                placeholder="Select an option",
                style={"marginBottom": "10px"}
            ),
            html.Button("Submit", id="submit-button", className="btn btn-primary")
        ], width=3),

        # Column 2
        dbc.Col([
            html.H5("Graph and Table"),
            dcc.Graph(id='my-graph'),
            dash_table.DataTable(
                id='my-table',
                columns=[{"name": i, "id": i} for i in ["A", "B", "C"]],
                data=[],
                style_table={"overflowX": "auto"},
                page_size=5
            )
        ], width=7),

        # Column 3
        dbc.Col([
            html.H5("Parameters"),
            dbc.Row([
                dbc.Col(input_grid[i], width=6) for i in range(6)
            ], className="g-2")  # g-2 adds gutters (spacing) between rows
        ], width=2)
    ])
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
