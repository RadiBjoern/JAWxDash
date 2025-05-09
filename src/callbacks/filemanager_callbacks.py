# Package import
from dash import html, callback, Output, Input, State

# Local import
import ids
from readers import parse_contents


@callback(
    Output(ids.Store.UPLOADED_FILES, 'data', allow_duplicate=True),
    Output(ids.Div.INFO, 'children', allow_duplicate=True),
    Input(ids.Upload.DRAG_N_DROP, 'contents'),
    State(ids.Upload.DRAG_N_DROP, 'filename'),
    State(ids.Store.UPLOADED_FILES, 'data'),
    prevent_initial_call=True,
)
def update_uploaded_files(contents, filename:str, current_data:dict):
    
    # check if the 'contents' is NOT none
    if contents != None:
        
        # iterate over the contents and filename pairs
        for content, file in zip(contents, filename):

            # check if the file is already loaded
            if file not in current_data:
                data = parse_contents(content, file)

                # check if 'data' is NOT none
                if data:
                    current_data[file] = data.to_dict()
        
        return current_data, html.Div("Uploaded: " + ', '.join([name for name in filename]))



@callback(
    Output(ids.Store.UPLOADED_FILES, 'data'),
    Output(ids.DropDown.UPLOADED_FILES, 'options'),
    Output(ids.Div.INFO, 'children'),
    Input(ids.Button.DELETE_SELECTED, 'n_clicks'),
    State(ids.DropDown.UPLOADED_FILES, 'value'),
    State(ids.Store.UPLOADED_FILES, 'data'),
    prevent_initial_call=True,
)
def delete_selected_from_list(_, selected_file, current_files):
    # Removing selected file from dropdown
    new_options = [f for f in current_files if f != selected_file]
    del current_files[selected_file]
    
    return current_files, new_options, html.Div(f"Deleted: {selected_file}")