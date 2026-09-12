import numpy as np

def majority_classifier(y_train: list[int], X_test: list) -> np.ndarray:
    """
    Predict the most frequent training label for every test sample.
    Returns a one-dimensional NumPy integer array.
    """

    if len(y_train) == 0:
        return np.array([], dtype=int)

    counts = {}

    for label in y_train:
        counts[label] = counts.get(label, 0) + 1

    majority_label = max(counts, key=counts.get)

    predictions = np.full(
        len(X_test),
        majority_label,
        dtype=int
    )

    return predictions