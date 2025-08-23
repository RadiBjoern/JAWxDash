import dash
from dash import Dash, html
import dash_table
import pandas as pd
from dash.dash_table.Format import Format, Group, Scheme, Symbol

# Sample data
df = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Price': [1234.5, 6789.01, 2345.67],
    'Discount': [0.1, 0.05, 0.2]
})


app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[
            {'name': 'Product', 'id': 'Product'},
            {
                'name': 'Price',
                'id': 'Price',
                'type': 'numeric',
                'format': Format(precision=2, scheme=Scheme.fixed, group=Group.yes, symbol=Symbol.yes, symbol_suffix=" $")
            },
            {
                'name': 'Discount',
                'id': 'Discount',
                'type': 'numeric',
                'format': Format(precision=1, scheme=Scheme.percentage)
            },
        ],
        style_cell={'textAlign': 'right', 'padding': '8px'},
        style_header={'fontWeight': 'bold'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
