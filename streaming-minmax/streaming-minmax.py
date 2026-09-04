import numpy as np


def streaming_minmax(D, batches, eps=1e-8):

    # Create minimum values initially as infinity
    running_min = np.full(D, np.inf)

    # Create maximum values initially as negative infinity
    running_max = np.full(D, -np.inf)

    # Empty list to store normalized batches
    normalized_batches = []

    # Go through each batch
    for batch in batches:

        # Convert batch into a NumPy array
        batch = np.array(batch)

        # Find and update the minimum value
        running_min = np.minimum(
            running_min,
            batch.min(axis=0)
        )

        # Find and update the maximum value
        running_max = np.maximum(
            running_max,
            batch.max(axis=0)
        )

        # Normalize the batch
        normalized = (
            batch - running_min
        ) / (
            running_max - running_min + eps
        )

        # Store the normalized batch
        normalized_batches.append(normalized)

    # Return the results
    return {
        "normalized_batches": normalized_batches,
        "min": running_min,
        "max": running_max
    }