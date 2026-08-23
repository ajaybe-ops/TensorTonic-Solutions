import numpy as np

def bigram_probabilities(tokens: list) -> dict:
    # Get sorted unique vocabulary
    vocab = sorted(set(tokens))
    V = len(vocab)

    # Create mapping: token -> index
    token_to_idx = {token: i for i, token in enumerate(vocab)}

    # Initialize count matrix
    counts = np.zeros((V, V), dtype=int)

    # Count adjacent bigrams
    for i in range(len(tokens) - 1):
        current_token = tokens[i]
        next_token = tokens[i + 1]

        row = token_to_idx[current_token]
        col = token_to_idx[next_token]

        counts[row, col] += 1

    # Add-1 smoothing
    probabilities = (counts + 1) / (
        counts.sum(axis=1, keepdims=True) + V
    )

    return {
        "vocab": vocab,
        "counts": counts,
        "probabilities": probabilities
    }