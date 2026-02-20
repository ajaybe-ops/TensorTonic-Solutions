def iou(box_a, box_b):
    """
    Compute Intersection over Union (IoU) of two bounding boxes.
    
    Parameters:
        box_a, box_b: iterable of length 4
            Format: (x1, y1, x2, y2)
            where (x1, y1) is top-left and (x2, y2) is bottom-right.
    
    Returns:
        float: IoU value in [0, 1]
    """

    # Intersection coordinates
    x_left   = max(box_a[0], box_b[0])
    y_top    = max(box_a[1], box_b[1])
    x_right  = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    # Compute intersection area
    inter_width  = max(0.0, x_right - x_left)
    inter_height = max(0.0, y_bottom - y_top)
    intersection = inter_width * inter_height

    # Compute areas of individual boxes
    area_a = max(0.0, box_a[2] - box_a[0]) * max(0.0, box_a[3] - box_a[1])
    area_b = max(0.0, box_b[2] - box_b[0]) * max(0.0, box_b[3] - box_b[1])

    # Union area
    union = area_a + area_b - intersection

    # Avoid division by zero
    if union == 0:
        return 0.0

    return intersection / union