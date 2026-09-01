import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    X = np.array(X, dtype=float)

    #Sample covariance matrix
    covariance = np.cov(X, rowvar=False)

    #adding some standard deviation of each feature
    std = np.sqrt(np.diag(covariance))

    #pearson correlation forumla adding here
    correlation = covariance / np.outer(std, std)

    return correlation