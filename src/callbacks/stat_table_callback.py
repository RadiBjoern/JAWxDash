from dash import callback, dash_table, Output, Input, State
from dash.dash_table.Format import Format, Scheme
import logging
import numpy as np
import pandas as pd

from src import ids
from src.utils.readers import JAWFile
from src.utils.edge_exclusion import create_masked_file


logger = logging.getLogger(__name__)


@callback(
    Output(ids.Div.STAT_TABLE, "children"),
    Input(ids.DropDown.UPLOADED_FILES, "value"),
    Input(ids.Store.SETTINGS, "data"),
    State(ids.Store.UPLOADED_FILES, "data"),
)
def update_stat_table(selected_file, settings, stored_files):

    if not selected_file:
        return None
    
    file = JAWFile.from_path_or_stream(stored_files[selected_file])

    if settings["ee_state"]:
        file = create_masked_file(file, settings)


    stat = file.stats()
    stat.pop("Point #")

    columns = [{"id": col, "name": col, "type": "numeric", "format": Format(precision=4, scheme=Scheme.fixed)} for col in stat.columns]
    
    
    data = stat.to_dict("records")


    table = dash_table.DataTable(
        columns=columns,
        data=data,
        style_table={'overflowX': 'auto'},
        style_cell={'padding': '8px', 'textAlign': 'right'},
        style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
    ),


    return table