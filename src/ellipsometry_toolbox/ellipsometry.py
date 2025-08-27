import pandas as pd
import io



# Local imports
from src.ellipsometry_toolbox.statistics import get_statistics
from src.ellipsometry_toolbox import ja_woollam as jaw
from src.ellipsometry_toolbox.linear_translations import rotate, translate



class Ellipsometry:

    @classmethod
    def from_path_or_stream(cls, path_or_stream:str|bytes):
        data = jaw.read_data(path_or_stream)

        return Ellipsometry(data)
    


    def __init__(self, data:pd.DataFrame):
        """
        This class is intended to hold the data from J.A.Woollam ellipsometer

        The data holds a header and a data section.
        """

        self.data = data

        return None
    


    def sanity_check(self) -> list[str]:
        """
        Method for checking if the imported data set is sound
        
        Check for dublicat x,y-coordinates
        """

        message = []

        # Test for coordinates
        xy_list = self.data.apply(lambda row: "%.4f,%.4f" % (row.x, row.y))
        for i, xy in enumerate(xy_list[:-1]):
            if xy in "\t".join(xy_list[i+1:]):
                message.append("Dublicate found: %s" % xy)

        return message



    def get_column_names(self) -> list[str]:
        """Returns as list of column names"""

        return self.data.columns.to_list()
    


    def offset(self, x:float=0, y:float=0, theta:float=0):
        """
        Rotates then translates the x,y coordinates
        
        Returns: np.ndarray [2,N]
        """
        
        xy = self.data[["x", "y"]].to_numpy()
        
        xy_rot = rotate(xy.T, theta)
        xy_rot_trans = translate(xy_rot, [x,y])

        
        return xy_rot_trans.T
    


    def statistics(self) -> pd.DataFrame:
        """
        Calculates the statistics of the ellipsometer data in the form of a pandas dataframe.

        Excluded are column 'x' and 'y', and 'Point #' defaults to N/A
        
        Index:
        - count
        - Average
        - Std dev
        - Min
        - 25%
        - 50%
        - 75%
        - Max
        - % Range
        - % Uniformity
        - CV
        - CV min-max
        """
        stats = get_statistics(self.data)

        # Schema for renaming index        
        index_names = {
            "mean": "Average", 
            "min": "Min", 
            "max": "Max", 
            "std": "Std. Dev.",
        }
        stats.rename(index=index_names, inplace=True)

        return stats
    


    def to_buffer(self) -> io.StringIO:
        """Returns as buffered version of the data set similar to the JAW file"""


        buffer = jaw.to_buffer(self.data)

        return buffer
