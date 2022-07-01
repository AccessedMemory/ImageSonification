import numpy as np
from scipy.signal import argrelextrema


def get_min_max_values(column,
                       n_min=6,
                       n_max=6):
    """ This method takes a column from the image and returns the minimum and maximum values.

    :param column: This is a single column from the image as a numpy array.
    :type column: np.array
    :param n_min: The number of low frequencies you want to sample form the column. (default :obj:`6`).
    :type n_min: positive int
    :param n_max: The number of high frequencies you want to sample form the column. (default :obj:`6`).
    :type n_max: positive int
    :param n_max:
    :return:
    """

    # Define scale factor (sf) between highest pitch and pixel intensity.
    pitch_sf = 7.74

    # Find the maxima and minima pixel intensities within the column
    extrema = argrelextrema(column, np.greater)

    # extrema is a tuple containing an array of the indices of the maxima
    max_values = column[extrema[0]]
    # Get the top n maxima
    idx = np.argpartition(max_values, -n_max)[-n_max:]
    # This is a list of the highest pixels intensities for this column
    max_values = max_values[idx]

    # Similar for minima
    min_values = column[extrema[0]]
    split_idx = int(np.floor(len(min_values) / 2))
    min_values_idx = np.argpartition(min_values, split_idx)[split_idx:split_idx + n_min]
    min_values = min_values[min_values_idx]

    # Combine extrema into one list
    extrema_values = np.multiply(pitch_sf, np.concatenate((max_values, min_values), axis=0))
    return extrema_values
