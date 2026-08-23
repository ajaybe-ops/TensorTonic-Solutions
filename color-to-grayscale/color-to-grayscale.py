def color_to_grayscale(image):
    result = []

    for row in image:
        gray_row = []

        for pixel in row:
            R, G, B = pixel
            gray = 0.299 * R + 0.587 * G + 0.114 * B
            gray_row.append(gray)

        result.append(gray_row)

    return result