import numpy as np

def sample_var_std(x: list) -> dict:
    mean = np.mean(x)

    variance = np.sum((np.array(x) - mean) ** 2) / (len(x) - 1)

    std_dev = np.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(std_dev)
    }
