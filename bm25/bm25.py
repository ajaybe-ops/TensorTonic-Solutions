import math
from collections import Counter
import numpy as np

def bm25_score(query_tokens: list[str], docs: list[list[str]],
               k1: float = 1.2, b: float = 0.75) -> np.ndarray:
    """
    Returns a NumPy array with one score per document.
    """

    N = len(docs)

    if N == 0:
        return np.array([])

    # Average document length
    avgdl = sum(len(doc) for doc in docs) / N

    # Repeated query terms are counted only once
    query_terms = set(query_tokens)

    # Document frequency: number of documents containing each term
    df = {
        term: sum(1 for doc in docs if term in doc)
        for term in query_terms
    }

    scores = []

    for doc in docs:
        doc_len = len(doc)
        term_counts = Counter(doc)

        score = 0.0

        for term in query_terms:
            tf = term_counts[term]

            if tf == 0:
                continue

            idf = math.log(
                (N - df[term] + 0.5) / (df[term] + 0.5) + 1
            )

            denominator = tf + k1 * (
                1 - b + b * doc_len / avgdl
            )

            score += idf * (
                tf * (k1 + 1) / denominator
            )

        scores.append(score)

    return np.array(scores)