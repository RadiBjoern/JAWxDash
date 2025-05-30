from dash import html, dcc
import dash_bootstrap_components as dbc


import ids

filemanager_layout = dbc.CardBody([
    # Drag-n-drop field
    dcc.Upload(
        id=ids.Upload.DRAG_N_DROP,
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '100px',
            'lineHeight': '100px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'backgroundColor': '#f8f9fa',
            'cursor': 'pointer'
        },            # Allow multiple files to be uploaded
        multiple=True
    ),
    # Vertical spacing
    html.Div(style={"height": "15px"}),
    
    # File dropdown
    dcc.Dropdown(
        id=ids.DropDown.UPLOADED_FILES,
        options=[],
        value='',
        multi=False,
        clearable=False,
        className="mb-3",
    ),
    # File delete button
    dbc.Button(
            "Delete Selected",
            id=ids.Button.DELETE_SELECTED,
            color="primary",
            className="w-100"
        ),
], className="mt-4", style={"maxWidth": "400px"})
