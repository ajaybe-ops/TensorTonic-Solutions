import numpy as np


def batch_generator(X: list, y: list, batch_size: int,
                    seed: int = 42, drop_last: bool = False):

    # Step 1: Convert X into a NumPy array
    X = np.array(X)

    # Step 2: Convert y into a NumPy array
    y = np.array(y)

    # Step 3: Create a random generator
    rng = np.random.default_rng(seed)

    # Step 4: Create shuffled positions
    indices = rng.permutation(len(X))

    # Step 5: Shuffle X
    X = X[indices]

    # Step 6: Shuffle y using the same positions
    y = y[indices]

    # Step 7: Create batches
    for start in range(0, len(X), batch_size):

        # Step 8: Find the end position
        end = start + batch_size

        # Step 9: Remove smaller last batch if required
        if drop_last and end > len(X):
            break

        # Step 10: Create X batch
        X_batch = X[start:end]

        # Step 11: Create y batch
        y_batch = y[start:end]

        # Step 12: Give one batch
        yield X_batch, y_batch