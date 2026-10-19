import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    rng = np.random.default_rng(seed)

    x_arr = np.array(x)
    n = len(x_arr)

    resamples = rng.choice(x_arr, size=(n_bootstrap, n), replace=True)

    bootstrap_mean = np.mean(resamples, axis=1)

    alpha = (1.0 - ci) / 2.0
    lower = np.quantile(bootstrap_mean, alpha)
    upper = np.quantile(bootstrap_mean, 1.0 - alpha)

    overall_bootstrap_mean = np.mean(bootstrap_mean)

    return {
        "bootstrap_mean":
float(overall_bootstrap_mean),
        "lower": float(lower),
        "upper": float(upper)
    }
    pass