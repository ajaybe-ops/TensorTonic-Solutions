import numpy as np

def mean_average_precision(y_true_list: list, y_score_list: list, k: int | None = None) -> dict:

    ap_per_query = []

    for y_true, y_score in zip(y_true_list, y_score_list):

        # Convert to NumPy arrays
        y_true = np.array(y_true)
        y_score = np.array(y_score)

        # Sort by score from highest to lowest
        sorted_indices = np.argsort(y_score)[::-1]

        # Rearrange true labels according to ranking
        y_true = y_true[sorted_indices]

        # IMPORTANT: Count total relevant items BEFORE applying k
        total_relevant = np.sum(y_true)

        # Decide how many ranks to check
        if k is None:
            limit = len(y_true)
        else:
            limit = min(k, len(y_true))

        relevant_count = 0
        precision_sum = 0.0

        # Calculate precision only up to k
        for rank in range(1, limit + 1):

            if y_true[rank - 1] == 1:

                relevant_count += 1

                precision = relevant_count / rank

                precision_sum += precision

        # Calculate AP
        if total_relevant == 0:
            ap = 0.0
        else:
            ap = precision_sum / total_relevant

        ap_per_query.append(float(ap))

    # Calculate MAP
    map_value = float(np.mean(ap_per_query))

    return {
        "map_value": map_value,
        "ap_per_query": ap_per_query
    }