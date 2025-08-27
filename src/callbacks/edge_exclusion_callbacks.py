from dash import callback, dcc, Input, Output, State
import logging
import os
import io
import zipfile


# Local imports
from src.ellipsometry_toolbox.ellipsometry import Ellipsometry
from src.ellipsometry_toolbox.masking import create_masked_file
from src import ids


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
    file = Ellipsometry.from_path_or_stream(stored_files[selected_file])
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

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:

            for selected_file in stored_files:

                # File output name
                root, ext = os.path.splitext(selected_file)
                filename = root + "_masked" + ext


                # Loading into JAWFile object
                file = Ellipsometry.from_path_or_stream(stored_files[selected_file])
                masked_file = create_masked_file(file, settings)

                buffer = masked_file.to_buffer()

                zf.writestr(filename, buffer.getvalue())

        
        zip_buffer.seek(0)
        
        return dict(content=zip_buffer.getvalue(), filename="ellipsometer_download.zip", type="application/zip")
        #return dcc.send_bytes(buffer.getvalue(), filename="multiple_files.zip")           
        

    else:
        """
        Single file processing
        """
        # File output name
        root, ext = os.path.splitext(selected_file)
        filename = os.path.join(root, "_masked", ext)
    

        # Loading into JAWFile object
        file = Ellipsometry.from_path_or_stream(stored_files[selected_file])
        masked_file = create_masked_file(file, settings)
        
        buffer = masked_file.to_buffer()
        
        return dcc.send_string(buffer.getvalue(), filename=filename)
