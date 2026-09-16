
def nms(boxes: list, scores: list, iou_threshold: float) -> list:
    # Step 1: Get the number of boxes
    n = len(boxes)

    # Step 2: Sort indices by score, highest first
    order = sorted(range(n), key=lambda i: scores[i], reverse=True)

    # Step 3: Store the selected original indices
    kept = []

    # Step 4: Process boxes in confidence order
    while order:
        # Select the highest-scoring remaining box
        current = order.pop(0)
        kept.append(current)

        remaining = []

        # Step 5: Compare with every remaining box
        for idx in order:
            # Get coordinates of both boxes
            x1 = max(boxes[current][0], boxes[idx][0])
            y1 = max(boxes[current][1], boxes[idx][1])
            x2 = min(boxes[current][2], boxes[idx][2])
            y2 = min(boxes[current][3], boxes[idx][3])

            # Calculate intersection area
            width = max(0, x2 - x1)
            height = max(0, y2 - y1)
            intersection = width * height

            # Calculate areas of both boxes
            area1 = max(0, boxes[current][2] - boxes[current][0]) * \
                    max(0, boxes[current][3] - boxes[current][1])

            area2 = max(0, boxes[idx][2] - boxes[idx][0]) * \
                    max(0, boxes[idx][3] - boxes[idx][1])

            # Calculate union area
            union = area1 + area2 - intersection

            # Calculate IoU
            iou = intersection / union if union > 0 else 0

            # Keep boxes whose IoU is below the threshold
            if iou < iou_threshold:
                remaining.append(idx)

        # Continue with boxes that were not suppressed
        order = remaining

    # Return original indices in selection order
    return kept