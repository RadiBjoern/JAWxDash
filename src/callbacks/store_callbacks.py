from dash import callback, Output, Input


from src import ids


@callback(
    Output(ids.DropDown.UPLOADED_FILES, 'options', allow_duplicate=True),
    Input(ids.Store.UPLOADED_FILES, 'data'),
    prevent_initial_call=True,
)
def update_listbox(current_data) -> list[str]:
    entries = list(current_data.keys())

    return sorted(entries)
