from collections import Counter
import math

def bleu_score(candidate, reference, max_n):
    candidate_length = len(candidate)
    reference_length = len(reference)

    # Edge case
    if candidate_length == 0:
        return 0.0

    precisions = []

    # 1. Calculate modified precision for n = 1 to max_n
    for n in range(1, max_n + 1):

        # If candidate is too short to create this n-gram
        if candidate_length < n:
            return 0.0

        # Create candidate n-grams
        candidate_ngrams = []
        for i in range(candidate_length - n + 1):
            ngram = tuple(candidate[i:i + n])
            candidate_ngrams.append(ngram)

        # Create reference n-grams
        reference_ngrams = []
        for i in range(reference_length - n + 1):
            ngram = tuple(reference[i:i + n])
            reference_ngrams.append(ngram)

        # Count occurrences
        candidate_counts = Counter(candidate_ngrams)
        reference_counts = Counter(reference_ngrams)

        # Clipped count
        clipped_count = 0
        for ngram, count in candidate_counts.items():
            clipped_count += min(count, reference_counts.get(ngram, 0))

        total_count = len(candidate_ngrams)

        # Avoid log(0)
        if clipped_count == 0:
            return 0.0

        precisions.append(clipped_count / total_count)

    # 2. Brevity Penalty
    c = candidate_length
    r = reference_length

    if c >= r:
        BP = 1.0
    else:
        BP = math.exp(1 - r / c)

    # 3. Geometric mean of precisions
    log_sum = sum(math.log(p) for p in precisions)
    geometric_mean = math.exp(log_sum / max_n)

    # Final BLEU score
    return BP * geometric_mean