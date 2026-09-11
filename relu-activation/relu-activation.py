import numpy as np

def relu(x) -> np.ndarray:
    x = np.array(x)
    return np.array(np.maximum(0, x))  #did convert into numpy array gerade, wichtig, relu(5) to array(5)