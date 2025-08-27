import numpy as np
import pandas as pd



def uniformity(arr:pd.Series) -> float:
    """
    Uniformity

    uniformity = sum((x-mean)**2)/n
    """

    sum_sq = np.sum((arr-arr.mean())**2)

    return sum_sq / len(arr)



def perc_range(arr:pd.Series) -> float:
    """
    Percentile range
    
    perc_range = (max-min)/mean * 100
    """

    return (arr.max()-arr.min())/arr.mean() * 100



def coefficient_variation(arr:pd.Series) -> float:
    """
    Calculates the coefficient of variation
    
    CV = std/mean
    """

    return arr.std()/arr.mean()



def cv_min_max(arr:pd.Series) -> float:
    """
    Calculates the coefficient of variation min-max
    
    cv_mm = (max - min) / (2*mean)
    """

    return (arr.max()-arr.min()) / (2*arr.mean())



def get_statistics(frame:pd.DataFrame) -> pd.DataFrame:
    """
    Uses the Pandas describe() function and adds:

    - % Range
    - % Uniformity
    - CV
    - CV min-max
    """

    # Generation the pandas part
    desc = frame.describe()

    # Generating the custrom part
    p_range = frame.apply(perc_range, axis=0)
    p_unif = frame.apply(uniformity, axis=0)
    cv = frame.apply(coefficient_variation, axis=0)
    cv_mm = frame.apply(cv_min_max, axis=0)

    index_names = {
        0: "% Range",
        1: "% Uniformity",
        2: "CV",
        3: "CV min-max",
    }
    cust = pd.concat([p_range, p_unif, cv, cv_mm], axis=1).T.rename(index=index_names)

    # Joining the pandas and custom part
    stats = pd.concat([desc, cust], axis=0)


    return stats




if __name__ == "__main__":
    data = dict(
        a=[1,2,3,4],
        b=[5,6,7,8]
    )

    df = pd.DataFrame(data)

    get_statistics(df)
