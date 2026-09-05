def calibrate_isotonic(cal_labels: list, cal_probs: list, new_probs: list) -> list:
    """
    Returns a list of calibrated probabilities.
    """

    # Combine probabilities and labels, then sort by probability
    pairs = sorted(zip(cal_probs, cal_labels))

    # Group identical probabilities together
    grouped = []

    for prob, label in pairs:
        if grouped and grouped[-1]["prob"] == prob:
            grouped[-1]["sum"] += label
            grouped[-1]["count"] += 1
        else:
            grouped.append({
                "prob": prob,
                "sum": label,
                "count": 1
            })

    # Pool Adjacent Violators (PAV) algorithm
    blocks = []

    for group in grouped:
        blocks.append(group.copy())

        # Merge blocks while monotonicity is violated
        while len(blocks) >= 2:
            mean1 = blocks[-2]["sum"] / blocks[-2]["count"]
            mean2 = blocks[-1]["sum"] / blocks[-1]["count"]

            if mean1 > mean2:
                # Merge the two blocks
                right = blocks.pop()
                left = blocks.pop()

                blocks.append({
                    "prob": right["prob"],
                    "sum": left["sum"] + right["sum"],
                    "count": left["count"] + right["count"]
                })
            else:
                break

    # Create fitted probabilities for every calibration probability
    fitted_probs = []
    fitted_values = []

    start = 0

    for block in blocks:
        mean = block["sum"] / block["count"]

        # Number of unique probability groups represented
        remaining_count = block["count"]

        # Recover probabilities belonging to this block
        # using their cumulative observation counts
        while start < len(grouped) and remaining_count > 0:
            fitted_probs.append(grouped[start]["prob"])
            fitted_values.append(mean)

            remaining_count -= grouped[start]["count"]
            start += 1

    # Calibrate new probabilities
    result = []

    for p in new_probs:

        # Clamp below calibration range
        if p <= fitted_probs[0]:
            result.append(fitted_values[0])

        # Clamp above calibration range
        elif p >= fitted_probs[-1]:
            result.append(fitted_values[-1])

        else:
            # Find neighbouring calibration points
            for i in range(len(fitted_probs) - 1):
                x1 = fitted_probs[i]
                x2 = fitted_probs[i + 1]

                if x1 <= p <= x2:
                    y1 = fitted_values[i]
                    y2 = fitted_values[i + 1]

                    # Linear interpolation
                    calibrated = y1 + (p - x1) * (y2 - y1) / (x2 - x1)

                    result.append(calibrated)
                    break

    return result