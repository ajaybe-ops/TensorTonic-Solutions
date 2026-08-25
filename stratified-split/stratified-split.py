import numpy as np

def stratified_split(X: list, y: list, test_size: float = 0.2, seed: int = 42) -> dict:
    rng = np.random.default_rng(seed)

    X = np.array(X)
    y = np.array(y)

    train_indices = []
    test_indices = []

    # Process each class separately
    for cls in np.unique(y):
        indices = np.where(y == cls)[0]

        # Shuffle indices of this class
        rng.shuffle(indices)

        # Calculate number of test samples
        n_test = round(len(indices) * test_size)

        # Keep at least one sample in training if class has > 1 sample
        if len(indices) > 1:
            n_test = min(n_test, len(indices) - 1)

        # Split indices
        test_indices.extend(indices[:n_test])
        train_indices.extend(indices[n_test:])

    # Sort final indices
    train_indices = np.sort(train_indices)
    test_indices = np.sort(test_indices)

    return {
        "X_train": X[train_indices],
        "X_test": X[test_indices],
        "y_train": y[train_indices],
        "y_test": y[test_indices]
    }