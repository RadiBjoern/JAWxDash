import base64
import io
import numpy as np
import os
import pandas as pd
import re
import uuid

from src.utils.utilities import rotate, translate, uniformity, perc_range, coefficient_variation, cv_min_max
from src.templates.settings_template import UPLOAD_DIRECTORY


class JAWFile:

    @classmethod
    def from_dict(cls, file:dict):
        return JAWFile(data=pd.DataFrame(data=file["data"]))
    
    

    @classmethod
    def from_path_or_stream(cls, path_or_stream:str|bytes):
        data = read_jaw_data(path_or_stream)

        return JAWFile(data)
    


    def __init__(self, data:pd.DataFrame):
        """
        This class is intended to hold the data from J.A.Woollam ellipsometer

        The data holds a header and a data section.
        """

        self.data = data

        return None
    


    def get_z_values(self) -> list:
        return list(self.data.columns.values)
    


    def offset(self, x:float=0, y:float=0, theta:float=0):
        """
        Rotates then translates the x,y coordinates
        
        Returns: np.ndarray [2,N]
        """
        
        xy = self.data[["x", "y"]].to_numpy()
        
        xy_rot = rotate(xy.T, theta)
        xy_rot_trans = translate(xy_rot, [x,y])

        
        return xy_rot_trans.T
    


    def stats(self) -> pd.DataFrame:
        """
        Calculates the statistics of the ellipsometer data in the form of a pandas dataframe.

        Excluded are column 'x' and 'y', and 'Point #' defaults to N/A
        
        Columns:
        - Point #
        - Z Align
        - SigIng
        - Tilt X
        - Tilt Y
        - Hardware OK
        - MSE
        - Thickness # 1 (nm)
        - A
        - B
        - n of Cauchy @ 632.8 nm
        - Fit OK

        Index:
        - Average
        - Min
        - Max
        - Std dev
        - %Range
        - %Uniformity
        - CV
        - CV min-max
        """
        data = self.data

        kwargs = dict(
            axis=0,
            skipna=True,
            numeric_only=True,
        )

        avg = data.mean(**kwargs)
        minimum = data.min(**kwargs)
        maximum = data.max(**kwargs)
        std = data.std(**kwargs)
        p_range = data.apply(perc_range, axis=0)
        p_unif = data.apply(uniformity, axis=0)
        cv = data.apply(coefficient_variation, axis=0)
        cv_mm = data.apply(cv_min_max, axis=0)
        
        col_names = {
            0: "Average", 
            1: "Min", 
            2: "Max", 
            3: "Std. Dev.",
            4: "% Range",
            5: "% Uniformity",
            6: "CV", 
            7: "CV min-max"
        }
        frames = (avg, minimum, maximum, std, p_range, p_unif, cv, cv_mm)
        stat = pd.concat(frames, axis="columns").T
        stat.rename(index=col_names, inplace=True)

        return stat
    


    def to_buffer(self) -> io.StringIO:
        
        buffer = io.StringIO()


        # Write header to buffer
        stats = self.stats()
        stats.drop(labels=["x", "y"], axis=1, inplace=True)
        stats.drop(labels=["CV", "CV min-max"], axis=0, inplace=True)
        stats.to_csv(buffer, sep="\t", float_format="%.4f", header=True, index=True)


        # Write data to buffer
        data = self.data
        xy_col = data.apply(lambda row: "(%.4f,%.4f)" % (row.x, row.y), axis=1)
        data.insert(0, "xy", xy_col)
        data.drop(labels=["x", "y"], axis=1, inplace=True)  # drops 'x' and 'y' column
        data.to_csv(buffer, sep="\t", header=False, index=False)


        return buffer
    


def read_jaw_data(filepath_or_stream:str|bytes) -> pd.DataFrame:
    """
    Read the jaw.TXT file from at filepath or a stream

    Returns a pd.DataFrame with columns:
    - Point #	
    - Z Align	
    - SigInt	
    - Tilt X	
    - Tilt Y	
    - Hardware OK	
    - MSE	
    - Thickness # 1 (nm)	
    - A	
    - B	
    - n of Cauchy @ 632.8 nm	
    - Fit OK

    """


    # Determines if filepath or stream
    lines = []
    filepath_or_buffer = ""
    if isinstance(filepath_or_stream, str):
        # is a path
        with open(filepath_or_stream, "r") as f:
            lines = f.readlines()
        filepath_or_buffer = filepath_or_stream

    
    elif isinstance(filepath_or_stream, bytes):
        # is a stream
        buffer = io.StringIO(filepath_or_stream.decode("utf-8"))
        lines = buffer.readlines()

        filepath_or_buffer = io.StringIO(filepath_or_stream.decode("utf-8"))
    


    # Find lines with the data, by matching (decimal,decimal)

    # Pattern explanation
    # \( and \): Match the parentheses that enclose the two numbers.
    # [+-]?: Matches an optional + or - sign before each number.
    # \d+\.\d+: Matches a decimal number (one or more digits before and after the decimal point).
    # ,: Matches the comma separating the two numbers.
    pattern = r"\([+-]?\d+(\.\d+)?,[+-]?\d+(\.\d+)?\)"

    data_line = False
    for i, line in enumerate(lines):
        matches = re.findall(pattern, line)
        if matches:
            data_line = i
            break

    # Reading header
    data = pd.read_csv(filepath_or_buffer, delimiter="\t", header=0, skiprows=range(1, data_line))


    # Extract x and y
    pattern = r"[-+]?(?:\d*\.*\d+)"

    x, y = [], []
    for i, xy in enumerate(data.iloc[:, 0].values.tolist()):
        matches = re.findall(pattern, xy)

        if len(matches) == 2:
            x.append(float(matches[0]))
            y.append(float(matches[1]))
        
        else:
            x.append(np.nan)
            y.append(np.nan)

            print(f"Bad pattern! row: {i}, string: {xy}, match: {matches}")

    # Adding x and y to DataFrame
    data['x'] = x
    data['y'] = y
    data.drop(data.columns[0], axis=1, inplace=True)  # drops first column with string (x.xxx, y.yyy) coordinates

    return data



#def parse_contents(contents, filename) -> JAWFile|None:
#    content_type, content_string = contents.split(',')
#    file = base64.b64decode(content_string)
#
#    # Assume the user uploaded a CSV file
#    if '.txt' in filename:
#        data = read_jaw_data(file)
#
#        return JAWFile(data)
#    
#    else:
#        # File type NOT supported
#        return None
    


def save_upload(content, filename):
    _, content_string = content.split(",")
    decoded = base64.b64decode(content_string)

    _, ext = os.path.splitext(filename)
    unique_name = "%s_%s" % (uuid.uuid4().hex, filename)

    file_path = os.path.join(UPLOAD_DIRECTORY, unique_name)

    with open(file_path, "wb") as f:
        f.write(decoded)
    
    return file_path
