from dash import html, dcc
import dash_bootstrap_components as dbc


import ids

filemanager_layout = dbc.Card([
    dbc.CardHeader("File Manager"),
    dbc.CardBody([
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
        html.Div(style={"height": "10px"}),
        
        # File dropdown
        dcc.Dropdown(
            id=ids.DropDown.UPLOADED_FILES,
            options=[],
            value='',
            multi=False,
            clearable=False,
            className="mb-0",
        ),
    
        # File delete button
        dbc.Button(
                "Delete Selected",
                id=ids.Button.DELETE_SELECTED,
                color="primary",
                className="mb-0 w-100"
        ),
    ])
], className="mt-1")

