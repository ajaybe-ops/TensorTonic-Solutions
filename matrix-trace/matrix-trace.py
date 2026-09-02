def matrix_trace(A: list) -> float:
    total = 0

    for i in range(len(A)):
        total += A[i][i]
        
    return float(total)