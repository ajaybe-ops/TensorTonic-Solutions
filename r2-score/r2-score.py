import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    y_mean = np.mean(y_true)

    ss_res = np.sum((y_true - y_pred) ** 2)

    ss_tot = np.sum((y_true - y_mean) ** 2)

    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0

    return float(1 - (ss_res / ss_tot))