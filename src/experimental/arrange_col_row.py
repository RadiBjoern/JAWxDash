import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def label_dropdown_row(label_text, dropdown_id, options):
    return dbc.Row(
        [
            dbc.Col(html.H6(label_text, className="mb-0"), width=2),
            dbc.Col(
                dcc.Dropdown(
                    id=dropdown_id,
                    options=[{"label": opt, "value": opt} for opt in options],
                    value=options[0],
                ),
                width=10,
            ),
        ],
        align="center",
        className="mb-2"
    )

app.layout = dbc.Container([
    label_dropdown_row("Select A:", "dropdown-a", ["A1", "A2", "A3"]),
    label_dropdown_row("Select B:", "dropdown-b", ["B1", "B2", "B3"]),
    label_dropdown_row("Select C:", "dropdown-c", ["C1", "C2", "C3"]),
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
