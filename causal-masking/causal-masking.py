import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    T = scores.shape[-1]
    
    # Create upper triangular mask (future positions)
    mask = np.triu(np.ones((T, T)), k=1).astype(bool)
    
    # Copy scores to avoid modifying original
    masked_scores = scores.copy()
    
    # Replace future positions directly
    masked_scores[..., mask] = mask_value
    
    return masked_scores.astype(float)