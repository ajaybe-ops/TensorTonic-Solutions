import numpy as np
from scipy.special import erf

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    
    """

    #lassen wir convert to a numpy array ,wanna make asrray operation arbeit this time
    x_arr = np.array(x)

    #so lets app;ly GELU gerade
    return 0.5 * x_arr * (1 + erf(x_arr / np.sqrt(2)))