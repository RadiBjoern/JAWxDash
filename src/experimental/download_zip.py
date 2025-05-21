import dash
from dash import html, dcc, Input, Output
import zipfile
import io
import base64

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button("Download Files", id="btn-download"),
    dcc.Download(id="download-zip")
])

@app.callback(
    Output("download-zip", "data"),
    Input("btn-download", "n_clicks"),
    prevent_initial_call=True
)
def generate_zip(n_clicks):
    # Files to include
    file_dict = {
        "file1.txt": "Content of file 1",
        "file2.txt": "Another file with text content",
        "notes/readme.md": "# This is a readme file"
    }

    # Create in-memory zip
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for filename, content in file_dict.items():
            zf.writestr(filename, content)
    buffer.seek(0)

    return dcc.send_bytes(buffer.getvalue(), filename="multiple_files.zip")

if __name__ == "__main__":
    app.run_server(debug=True)
