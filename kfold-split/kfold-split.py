import numpy as np


def kfold_split(N, k, shuffle=True, seed=0):

    # Step 1: Create indices
    indices = np.arange(N)

    # Step 2: Shuffle indices
    if shuffle:
        rng = np.random.default_rng(seed)
        indices = rng.permutation(indices)

    # Step 3: Calculate fold sizes
    fold_sizes = np.full(k, N // k)

    # Step 4: Add extra samples to first folds
    fold_sizes[:N % k] += 1

    # Step 5: Create empty list
    folds = []

    # Step 6: Starting position
    start = 0

    # Step 7: Create each fold
    for fold_size in fold_sizes:

        # Find where this fold ends
        end = start + fold_size

        # Validation indices
        val_idx = indices[start:end]

        # Training indices
        train_idx = np.concatenate(
            (indices[:start], indices[end:])
        )

        # Save the fold
        folds.append({
            "train_idx": train_idx,
            "val_idx": val_idx
        })

        # Move to the next fold
        start = end

    return folds