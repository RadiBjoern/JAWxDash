from dash import Dash, dcc, html

# Local import
import ids
from layouts import filemanager_layout, graph_layout, sample_layout, spot_layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    # Initiating 'Store' for holding uploaded files i.e. *.txt and *.csv
    dcc.Store(id=ids.Store.UPLOADED_FILES, data={}),

    # Left column
    html.Div(
        [
            filemanager_layout,
        ], 
        style={
            'width': '15%', 
            'display': 'inline-block', 
            'verticalAlign': 'top', 
            'padding': '10px'
        }
    ),

    # Middle column
    html.Div(
        [
            # Main graph window
            graph_layout,
        ], 
        style={
            'width': '60%', 
            'display': 'inline-block', 
            'verticalAlign': 'top', 
            'padding': '10px'
        }
    ),

    # Right column
    html.Div(
        [
            spot_layout,
            sample_layout,
        ], 
        style={
            'width': '20%', 
            'display': 'inline-block', 
            'verticalAlign': 'top', 
            'padding': '10px'
        }
    ),
    
    # Bottom info panel
    html.Div(
        id=ids.Div.INFO, 
        style={'border': '1px solid black', 'padding': '10px', 'marginTop': '20px'}
    ),

])  #, className="app-container")


# Register callbacks
import callbacks.filemanager_callbacks
import callbacks.graph_callbacks
import callbacks.store_callbacks

if __name__ == '__main__':
    app.run(debug=True)
