
import math


def rotate_image(image: list, angle_degrees: float) -> list:
    # 1. Get the image dimensions
    H = len(image)
    W = len(image[0])

    # 2. Find the center of the image
    cy = (H - 1) / 2
    cx = (W - 1) / 2

    # 3. Convert degrees to radians
    theta = math.radians(angle_degrees)

    # 4. Calculate sine and cosine
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    # 5. Create an output image filled with zeros
    result = [[0] * W for _ in range(H)]

    # 6. Visit every pixel in the output image
    for i in range(H):
        for j in range(W):

            # 7. Find the position relative to the center
            dy = i - cy
            dx = j - cx

            # 8. Find the corresponding source position
            src_y = cy + dy * cos_t + dx * sin_t
            src_x = cx - dy * sin_t + dx * cos_t

            # 9. Find the nearest pixel
            src_y = round(src_y)
            src_x = round(src_x)

            # 10. Check whether the pixel is inside the image
            if 0 <= src_y < H and 0 <= src_x < W:

                # 11. Copy the pixel
                result[i][j] = image[src_y][src_x]

    # 12. Return the rotated image
    return result