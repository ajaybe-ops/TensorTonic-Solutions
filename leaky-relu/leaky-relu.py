import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky RELU values as a Numpy array matching the input shape.
    
    """

    #am gonna gerade convert input to a numpy array to ensure array operation arbeits good
    x_arr = np.array(x)

    #applying the leaky RELU formula: x if x> 0, else alpha * x
    return np.where(x_arr > 0, x_arr, x_arr * alpha)