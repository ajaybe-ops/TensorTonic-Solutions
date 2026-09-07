import numpy as np

def expected_calibration_error(y_true: list, y_pred: list, n_bins: int) -> float:

    # Create bins
    bin_edges = np.linspace(0, 1, n_bins + 1)

    total_error = 0
    n = len(y_true)

    # Go through every bin
    for i in range(n_bins):

        lower = bin_edges[i]
        upper = bin_edges[i + 1]

        # Find predictions inside this bin
        if i == n_bins - 1:
            mask = (np.array(y_pred) >= lower) & (np.array(y_pred) <= upper)
        else:
            mask = (np.array(y_pred) >= lower) & (np.array(y_pred) < upper)

        # Get values inside the bin
        bin_true = np.array(y_true)[mask]
        bin_pred = np.array(y_pred)[mask]

        # Only calculate if the bin contains predictions
        if len(bin_true) > 0:

            # Actual accuracy in the bin
            accuracy = np.mean(bin_true)

            # Average predicted confidence
            confidence = np.mean(bin_pred)

            # Add weighted calibration error
            total_error += (len(bin_true) / n) * abs(accuracy - confidence)

    return float(total_error)