from dash import html, dcc

import ids

filemanager_layout = html.Div(
    [
        # Drag-n-drop field
        dcc.Upload(
            id=ids.Upload.DRAG_N_DROP,
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '10px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),


        # File dropdown
        dcc.Dropdown(
            id=ids.DropDown.UPLOADED_FILES,
            options=[],
            value='',
            multi=False,
            clearable=False,
        ),
        

        # File delete button
        html.Button(
            "Delete Selected",
            id=ids.Button.DELETE_SELECTED,
        ),
    ],
)