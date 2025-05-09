from dash import Dash, dcc, html

# Local import
from buttons import delete_selected
from divs import info_panel
from dropdowns import file_listbox, colormaps, sample_outline, z_data
import graphs
from spot.spot_layout import spot_settings

from stores import files_store
from uploads import drag_n_drop


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # Initiating 'Store' for holding uploaded files i.e. *.txt and *.csv
    files_store,

    # Left column
    html.Div(
        [
            drag_n_drop,
            delete_selected,
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
            file_listbox,
            graphs.layout,
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
            spot_settings,
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



if __name__ == '__main__':
    app.run(debug=True)
