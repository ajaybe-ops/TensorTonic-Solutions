def detect_drift(reference_counts: list, production_counts: list, threshold: float) -> dict:
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)

    score = 0.0

    for ref, prod in zip(reference_counts, production_counts): 
        p = ref / ref_total
        q = prod / prod_total
        score += abs(p - q)

    score *= 0.5

    return {
        "score": score,
        "drift_detected": score > threshold
    }