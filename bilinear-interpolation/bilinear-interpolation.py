def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    H = len(image)
    W = len(image[0])
    if new_h == 1:
        y_ratio = 0
    else:
        y_ratio = (H - 1) / (new_h - 1)
    if new_w == 1:
        x_ratio = 0
    else:
        x_ratio = (W - 1) / (new_w - 1)

    result = []
    for i in range(new_h):
        row = []
        for j in range(new_w):
            src_y = i * y_ratio
            src_x = j * x_ratio

            y0 = int(src_y)
            x0 = int(src_x)
            y1 = min(y0 + 1, H - 1)
            x1 = min(x0 + 1, W - 1)

            dy = src_y - y0
            dx = src_x - x0

            top = image[y0][x0] * (1 - dx) + image[y0][x1] * dx
            bottom = image[y1][x0] * (1 - dx) + image[y1][x1] * dx
            value = top * (1 - dy) + bottom * dy

            row.append(value)
        result.append(row)
    return result


# Example usage
image = [[0, 10], [20, 30]]
resized = bilinear_resize(image, 4, 4)
for row in resized:
    print(row)