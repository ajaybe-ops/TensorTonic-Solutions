import numpy as np 

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    g = np.asarray(g, dtype=float)

    norm = np.linalg.norm(g)  #calculated size of gradients
 
    if norm <= max_norm:  #did need to check if gradient size smaller than or = to allowed max
        return g

    return g * (max_norm / norm)