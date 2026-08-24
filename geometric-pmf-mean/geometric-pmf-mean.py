import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
  pmf = np.array([(1 - p) ** (x - 1) * p for x in k])
  mean = 1 / p
  
  return {
      "pmf": pmf,
      "mean": float(mean)
  }