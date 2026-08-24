import numpy as np

def detect_skew(train_dist: dict, serving_dist: dict, threshold: float = 0.2, eps: float = 1e-10) -> dict:
    """
    Returns a dictionary of feature PSI scores and skew flags.
    """
    result = {}

    for feature in train_dist:
        train = np.array(train_dist[feature], dtype=float)
        serving = np.array(serving_dist[feature], dtype=float)

        # Add epsilon to avoid log(0) and division by zero
        train_safe = train + eps
        serving_safe = serving + eps

        # PSI = Σ (s_i - t_i) * ln(s_i / t_i)
        psi = np.sum(
            (serving_safe - train_safe) *
            np.log(serving_safe / train_safe)
        )

        result[feature] = {
            "psi": round(float(psi), 6),
            "skewed": bool(psi >= threshold)
        }

    return result