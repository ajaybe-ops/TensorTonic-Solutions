
import math

def gaussian_kernel(size: int, sigma: float) -> list:
    kernel = []
    center = size // 2
    total = 0.0

    # Step 1: Calculate the Gaussian weight at each position
    for i in range(size):
        row = []

        for j in range(size):
            x = i - center
            y = j - center

            weight = math.exp(
                -(x**2 + y**2) / (2 * sigma**2)
            )

            row.append(weight)
            total += weight

        kernel.append(row)

    # Step 2: Normalize all the weights
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= total

    return kernel