import numpy as np


def one_hot(y: list, num_classes=None) -> np.ndarray:

    y = np.array(y)

    if num_classes is None:
        num_classes = max(y) + 1

    result = np.zeros((len(y), num_classes))

    for i in range(len(y)):
        result[i, y[i]] = 1

    return result