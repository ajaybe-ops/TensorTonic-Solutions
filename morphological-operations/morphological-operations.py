def morphological_op(image, kernel, operation):
    # Normalize the operation name
    op = operation.strip().lower()

    if op in ("erosion", "erode"):
        is_erosion = True
    elif op in ("dilation", "dilate"):
        is_erosion = False
    else:
        raise ValueError(f"Invalid operation: {operation}")

    rows = len(image)
    cols = len(image[0])
    k_rows = len(kernel)
    k_cols = len(kernel[0])

    pad_r = k_rows // 2
    pad_c = k_cols // 2

    # Create a zero-padded image
    padded = [
        [0 for _ in range(cols + 2 * pad_c)]
        for _ in range(rows + 2 * pad_r)
    ]

    for i in range(rows):
        for j in range(cols):
            padded[i + pad_r][j + pad_c] = image[i][j]

    result = []

    for i in range(rows):
        result_row = []

        for j in range(cols):
            values = []

            for ki in range(k_rows):
                for kj in range(k_cols):
                    # Only use kernel positions containing 1
                    if kernel[ki][kj] == 1:
                        pixel = padded[i + ki][j + kj]
                        values.append(pixel)

            if is_erosion:
                result_row.append(int(all(values)))
            else:
                result_row.append(int(any(values)))

        result.append(result_row)

    return result