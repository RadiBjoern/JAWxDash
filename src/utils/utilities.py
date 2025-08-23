# Library imports
import numpy as np


def uniformity(arr:np.ndarray):
    """
    Uniformity

    uniformity = sum((x-mean)**2)/n
    """

    mean = np.mean(arr)
    sum_sq = np.sum((arr-mean)**2)
    return sum_sq / len(arr)



def perc_range(arr:np.ndarray):
    """
    Percentile range
    
    perc_range = (max-min)/mean * 100
    """

    return (np.max(arr)-np.min(arr))/np.mean(arr) * 100


def coefficient_variation(arr:np.ndarray):
    """
    Calculates the coefficient of variation
    
    CV = std/mean
    """

    return np.std(arr)/np.mean(arr)


def cv_min_max(arr:np.ndarray):
    """
    Calculates the coefficient of variation min-max
    
    cv_mm = (max - min) / (2*mean)
    """

    return (np.max(arr)-np.min(arr)) / (2*np.mean(arr))



def gen_spot(x:float, y:float, color, dia_beam:float, angle_incident:float) -> dict:
    minor = dia_beam
    major = dia_beam / np.cos(np.deg2rad(angle_incident))

    x0 = x - 0.5*major
    x1 = x + 0.5*major
    y0 = y - 0.5*minor
    y1 = y + 0.5*minor

    return dict(
        type='circle',
        x0=x0,
        y0=y0,
        x1=x1,
        y1=y1,
        line=dict(
            color=color,
            width=1,
            dash='solid',
        ),
        fillcolor=color,
        name="spot",
    )



def rotate(xy:np.ndarray, angle:float) -> np.ndarray:
    """
    Rotates a Numpy array [N,2] 'angle' degree around (0, 0)
    xy: np.ndarray dimension [N,2] containing x and y coordinates
    angle: float rotational angle in degrees
    return: rotated version of xy
    """

    # Return if angle is 0
    if angle == 0:
        return xy
    

    assert xy.shape[0] == 2, f"Expected shape (2,N), but {xy.shape} were given."

    def rotator(array2d:np.ndarray) -> np.ndarray:
        rad = np.deg2rad(angle)
        A = np.array([
            [np.cos(rad), -np.sin(rad)],
            [np.sin(rad), np.cos(rad)]
        ])
        return np.dot(A, array2d)
    
    rotated_array = np.apply_along_axis(rotator, axis=0, arr=xy)
    
    assert rotated_array.shape[0] == 2, f"Rotated array shape should be (2,N), but get {rotated_array.shape}."
    
    
    return rotated_array



def translate(xy:np.ndarray, offset:np.ndarray|list[float]) -> np.ndarray:
    """
    Translates Numpy array [2, N] 'offset' amount
    xy: np.ndarray dimension [2, N] containing x and y coordinates
    offset: np.ndarray dimension [2, 1] containing offset
    return: translated version of xy
    """

    if offset[0] == 0 and offset[1] == 0:
        return xy

    # Check that xy is of type np.ndarray)
    if not isinstance(xy, np.ndarray):
        xy = np.asarray(xy)

    assert xy.shape[0] == 2, f"Expected shape (2,N), but {xy.shape} were given."

    def translator(array2d:np.ndarray) -> np.ndarray:
        return offset + array2d
    
    translated_array = np.apply_along_axis(translator, axis=0, arr=xy)

    assert translated_array.shape[0] == 2, f"Translated array shape should be (2,N), but get {translated_array.shape}."


    return translated_array

