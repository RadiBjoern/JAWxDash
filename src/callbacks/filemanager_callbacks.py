# Package import
from dash import html, callback, Output, Input, State, ctx

# Local import
from src import ids
from src.utils.readers import parse_contents, save_upload


@callback(
    Output(ids.Store.UPLOADED_FILES, 'data', allow_duplicate=True),
    Output(ids.Div.INFO, 'children', allow_duplicate=True),
    Input(ids.Upload.DRAG_N_DROP, 'contents'),
    State(ids.Upload.DRAG_N_DROP, 'filename'),
    State(ids.Store.UPLOADED_FILES, 'data'),
    prevent_initial_call=True,
)
def update_uploaded_files(contents, filenames:str, stored_files:dict):
    
    # check if the 'contents' is NOT none
    if not contents:
        return stored_files
        
    # iterate over the contents and filename pairs
    for content, filename in zip(contents, filenames):

        # check if the file is already loaded
        if filename not in stored_files:
            path = save_upload(content, filename)

            stored_files[filename] = path
    

    return stored_files, html.Div("Uploaded: " + ', '.join([name for name in filenames]))



@callback(
    Output(ids.Store.UPLOADED_FILES, 'data'),
    Output(ids.DropDown.UPLOADED_FILES, 'options'),
    Output(ids.Div.INFO, 'children'),
    Input(ids.Button.DELETE_SELECTED, 'n_clicks'),
    Input(ids.Button.CLEAR_FILE_MANAGER, "n_clicks"),
    State(ids.DropDown.UPLOADED_FILES, 'value'),
    State(ids.Store.UPLOADED_FILES, 'data'),
    prevent_initial_call=True,
)
def delete_selected_from_list(delete, clear, selected_file, current_files):

    triggered_id = ctx.triggered_id  # This tells you which button was clicked

    # Removing selected file from dropdown
    if triggered_id == ids.Button.DELETE_SELECTED:

        new_options = [f for f in current_files if f != selected_file]
        del current_files[selected_file]

        return current_files, new_options, html.Div(f"Deleted: {selected_file}")
    

    elif triggered_id == ids.Button.CLEAR_FILE_MANAGER:
        return {}, [], html.Div("File manager was cleared")
