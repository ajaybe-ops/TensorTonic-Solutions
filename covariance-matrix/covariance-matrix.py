import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    X = np.array(X)

    #Centering each feature
    mean = np.mean(X, axis=0)
    X_c = X - mean

    #Computing simple covariance matrix
    N = X.shape[0]
    covariance = (X_c.T @ X_c) / (N - 1)

    return covariance