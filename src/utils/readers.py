import base64
import io
import numpy as np
import os
import pandas as pd
import re
import uuid

from src.utils.utilities import rotate, translate
from src.templates.settings_template import UPLOAD_DIRECTORY


class JAWFile:

    @classmethod
    def from_dict(cls, file:dict):
        return JAWFile(
            header=file["header"],
            data=pd.DataFrame(data=file["data"]),
        )
    
    
    @classmethod
    def from_csv(cls, file):
        header, data = read_jaw_file(file)

        return JAWFile(header, data)
    

    @classmethod
    def from_stream(cls, stream):
        header, data = read_jaw_stream(stream)

        return JAWFile(header, data)
    

    def __init__(self, header:str, data:pd.DataFrame):
        """
        This class is intended to hold the data from J.A.Woollam ellipsometer

        The data holds a header and a data section.
        """

        self.header = header
        self.data = data

        return None
    

    def to_dict(self):
        return dict(
            header=self.header,
            data=self.data.to_dict(orient="list"),
        )
    

    def content(self):
        data_list = ["\t".join(map(str, row)) + "\n" for row in self.data.itertuples(index=False)]

        return "".join(self.header) + "".join(data_list)
    

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
    

    def update_header(self) -> None:
        """
        Updates the header will update the following:
        - Average
        - Min
        - Max
        - Std. Dev.

        Sets a new header 
        """

        # Generating the state for the columns
        average = ["%.4f" % self.data[col].mean() for col in self.data.columns if (self.data[col].dtypes == float) and (col != "Point #")]
        minimum = ["%.4f" % self.data[col].min()  for col in self.data.columns if (self.data[col].dtypes == float) and (col != "Point #")]
        maximum = ["%.4f" % self.data[col].max()  for col in self.data.columns if (self.data[col].dtypes == float) and (col != "Point #")]
        std_dev = ["%.4f" % self.data[col].std()  for col in self.data.columns if (self.data[col].dtypes == float) and (col != "Point #")]


        # Removing the stat for the "Point #"
        #average.pop(1)
        #minimum.pop(1)
        #maximum.pop(1)
        #std_dev.pop(1)


        # Generate new header
        new_header = [
            " \t" + self.header[0].strip() + "\n",
            "Average\t" + "\t".join(average) + "\n",
            "Min\t" + "\t".join(minimum) + "\n",
            "Max\t" + "\t".join(maximum) + "\n",
            "Std. Dev.\t" + "\t".join(std_dev) + "\n",
            self.header[5].strip() + "\n",
            self.header[6].strip() + "\n",
        ]


        # Setting new header
        self.header = new_header


        return None



def read_jaw_file(file):
    """
    Read a *.txt file from the JAW instrument
    """
    with open(file, "r") as f:
        lines = f.readlines()
    
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
    header = lines[:data_line]
    data = pd.read_csv(file, delimiter="\t", header=0, skiprows=range(1, data_line))


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

    return header, data



def read_jaw_stream(stream:bytes):
    """
    Read a *.txt io-stream from the JAW instruments
    
    Returns: Header[list], Data[Pandas.DataFrame]
    """

    # Opening file and reading into list
    buffer = io.StringIO(stream.decode("utf-8"))
    lines = buffer.readlines()
    

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
    header = lines[:data_line]


    # Reading the file with Pandas
    data = pd.read_csv(io.StringIO(stream.decode("utf-8")), delimiter="\t", header=0, skiprows=range(1, data_line))
    
    
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

    return header, data



def parse_contents(contents, filename) -> JAWFile|None:
    content_type, content_string = contents.split(',')
    file = base64.b64decode(content_string)

    # Assume the user uploaded a CSV file
    if '.txt' in filename:
        header, data = read_jaw_stream(file)

        return JAWFile.from_dict({"header": header, "data": data})
    
    else:
        # File type NOT supported
        return None
    


def save_upload(content, filename):
    _, content_string = content.split(",")
    decoded = base64.b64decode(content_string)

    _, ext = os.path.splitext(filename)
    unique_name = "%s_%s" % (uuid.uuid4().hex, filename)

    file_path = os.path.join(UPLOAD_DIRECTORY, unique_name)

    with open(file_path, "wb") as f:
        f.write(decoded)
    
    return file_path
