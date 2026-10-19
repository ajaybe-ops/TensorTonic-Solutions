from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean_val = np.mean(x)

    median_val = np.median(x)

    counts = Counter(x)
    max_freq = max(counts.values())

    mode_val = min(num for num, freq in counts.items() if freq == max_freq)

    return {
        "mean": float(mean_val),
        "median": float(median_val),
        "mode": float(mode_val)
    }