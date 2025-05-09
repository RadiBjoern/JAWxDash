from dash import Dash, html

# Local import
from divs import info_panel
from dropdowns import colormaps, sample_outline, z_data

from layouts import filemanager_layout, graph_layout, spot_layout

from stores import files_store


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # Initiating 'Store' for holding uploaded files i.e. *.txt and *.csv
    files_store,

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
            html.H6("Colormap", style={'textAlign': 'center',}),
            colormaps,
            html.H6("Sample outline", style={'textAlign': 'center',}),
            sample_outline,
            html.H6("Z-Data", style={'textAlign': 'center',}),
            z_data,
        ], 
        style={
            'width': '20%', 
            'display': 'inline-block', 
            'verticalAlign': 'top', 
            'padding': '10px'
        }
    ),
    
    # Bottom info panel
    info_panel
])


# Register callbacks
import callbacks.filemanager_callbacks
import callbacks.graph_callbacks


if __name__ == '__main__':
    app.run(debug=True)
