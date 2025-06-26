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
    
    file = JAWFile.from_csv(stored_files[selected_file])

    if settings["ee_state"]:
        file = create_masked_file(file, settings)

    tmp_data = file.data.select_dtypes(include=["float64", "int64"])
    tmp_data.drop(columns=["Point #"], inplace=True)

    minimum = tmp_data.min(axis=0)
    maximum = tmp_data.max(axis=0)
    mean = tmp_data.mean(axis=0)
    std = tmp_data.std(axis=0)

    mask = mean.abs() <= 1e-6
    if any(mask):
        logger.warning("Overflow error detected")

    cv = std/mean*100
    cv_mm = (maximum - minimum) / (2*mean) * 100

    cv[mask] = np.nan
    cv_mm[mask] = np.nan

    stat = pd.concat([mean, std, cv, cv_mm,minimum,maximum], axis=1).T
    stat.insert(0, "Stats", ["Mean", "Std.", "CV [%]", "CV_max-min [%]","min.","max."])


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