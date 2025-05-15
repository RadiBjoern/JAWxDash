from dash import callback, Input, Output, State


import ids


@callback(
    #Output(ids.Download.EDGE_EXCLUDED_FILE, "data"),
    Input(ids.Button.APPLY_EDGE_EXCLUSION, "n_clicks"),
    State(ids.DropDown.UPLOADED_FILES, "value"),
    State(ids.Store.UPLOADED_FILES, "data"),
    State(ids.Store.SETTINGS, "data"),
)
def download_edge_exclusion(n_clicks, selected_file:str, stored_files:dict, settings:dict):
    print("Apply edge exclusion btn-triggered")


    # check if a file is selected
    if not selected_file:
        return None
    

    file = stored_files[selected_file]

    data = file["data"]
    print(data)

    return None
