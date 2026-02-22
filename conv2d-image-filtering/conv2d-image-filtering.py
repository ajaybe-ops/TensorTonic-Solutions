def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    Returns a 2D Python list.
    """
    # Dimensions
    H, W = len(image), len(image[0])
    kH, kW = len(kernel), len(kernel[0])
    
    # Flip the kernel for convolution
    flipped_kernel = [[kernel[kH - 1 - i][kW - 1 - j] for j in range(kW)] for i in range(kH)]
    
    # Add padding
    padded_H = H + 2 * padding
    padded_W = W + 2 * padding
    padded_image = [[0]*padded_W for _ in range(padded_H)]
    for i in range(H):
        for j in range(W):
            padded_image[i + padding][j + padding] = image[i][j]
    
    # Output dimensions
    out_height = (padded_H - kH) // stride + 1
    out_width  = (padded_W - kW) // stride + 1
    output = [[0 for _ in range(out_width)] for _ in range(out_height)]
    
    # Convolution
    for i in range(out_height):
        for j in range(out_width):
            val = 0
            for m in range(kH):
                for n in range(kW):
                    val += padded_image[i*stride + m][j*stride + n] * flipped_kernel[m][n]
            output[i][j] = val
    
    return output