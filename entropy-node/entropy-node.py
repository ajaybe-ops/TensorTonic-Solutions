import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the shannon entropy as a python float gerade.
    """
    if len(y) == 0:
        return 0.0

    _, counts = np.unique(y, return_counts=True)

    probabilites = counts / len(y)

    entropy = -np.sum(probabilites * np.log2(probabilites))

    return float(entropy)