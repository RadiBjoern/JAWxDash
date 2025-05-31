from dash import callback, dcc, Input, Output, State
import logging
from io import StringIO
import os
import io
import zipfile

from utils.readers import JAWFile
from utils.edge_exclusion import create_masked_file
import ids


logger = logging.getLogger(__name__)


@callback(
        Output(ids.Text.EXCLUDED_POINTS, "children"),
        Input(ids.DropDown.UPLOADED_FILES, "value"),
        Input(ids.Store.SETTINGS, "data"),
        State(ids.Store.UPLOADED_FILES, "data"),
)
def update_excluded_points_text(selected_file:str, settings:dict, stored_files:dict) -> str:

    # check if a file is selected and edge exclusion is turned on
    if not selected_file or not settings["ee_state"]:
        return ""
    
    # Loading into JAWFile object
    file = JAWFile.from_dict(stored_files[selected_file])
    out_file = create_masked_file(file, settings)


    return "%i/%i" % (len(file.data.index) - len(out_file.data.index), len(file.data.index))



@callback(
    Output(ids.Download.EDGE_EXCLUDED_FILE, "data"),
    Input(ids.Button.DOWNLOAD_MASKED_DATA, "n_clicks"),
    State(ids.DropDown.UPLOADED_FILES, "value"),
    State(ids.Store.UPLOADED_FILES, "data"),
    State(ids.Store.SETTINGS, "data"),
)
def download_edge_exclusion(n_clicks, selected_file:str, stored_files:dict, settings:dict):
    

    # check if a file is selected and edge exclusion is turned on
    if not selected_file or not settings["ee_state"]:
        return None



    if settings["batch_processing"]:
        """
        Batch processing is selected and all the files in the 'file_manager' will be processed
        and downloaded as a zip-file
        """

        file_dict = {}
        for selected_file in stored_files:

            # File output name
            root, ext = os.path.splitext(selected_file)
            filename = root + "_masked" + ext


            # Loading into JAWFile object
            file = JAWFile.from_dict(stored_files[selected_file])
            out_file = create_masked_file(file, settings)

            out_file.data.drop(["x", "y"], axis="columns")
            
            file_dict[filename] = out_file.content()

        
        # Create in-memory zip
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as zf:
            for filename, content in file_dict.items():
                zf.writestr(filename, content)
        
        buffer.seek(0)
        
        return dcc.send_bytes(buffer.getvalue(), filename="multiple_files.zip")           
        

    else:
        """
        Single file processing
        """
        # File output name
        root, ext = os.path.splitext(selected_file)
        filename = os.path.join(root, "_masked", ext)
    

        # Loading into JAWFile object
        file = JAWFile.from_dict(stored_files[selected_file])
        out_file = create_masked_file(file, settings)

        out_file.data.drop(["x", "y"], axis="columns")

        # Build the output manually
        buffer = StringIO()


        # 1. Write header
        for line in out_file.header:
            buffer.write(line)

        # 2. Write data rows
        for row in out_file.data.itertuples(index=False):
            buffer.write("\t".join(map(str, row)) + "\n")


        buffer.seek(0)
        
        return dcc.send_string(buffer.getvalue(), filename=filename)
