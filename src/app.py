from dash import Dash, dcc, html, dash_table

# Local import
import ids
from logger_config import setup_logging
from layouts import edge_exclusion_layout, filemanager_layout, graph_layout, outline_layout, spot_layout, mappattern_layout, stat_table_layout, stage_layout


from templates.settings_template import DEFAULT_SETTINGS


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
setup_logging()  # initiate logging module

app = Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([
    # Initiating 'Store' for holding uploaded files i.e. *.txt and *.csv
    dcc.Store(id=ids.Store.UPLOADED_FILES, data={}, storage_type="session"),
    dcc.Store(id=ids.Store.DEFAULT_SETTINGS, data=DEFAULT_SETTINGS),
    dcc.Store(id=ids.Store.SETTINGS, data={}),

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
            stat_table_layout,
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
            outline_layout,
            stage_layout,
            mappattern_layout,
            edge_exclusion_layout,
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
import callbacks.settings_callback
import callbacks.edge_exclusion_callbacks


if __name__ == '__main__':
    app.run(debug=True)
