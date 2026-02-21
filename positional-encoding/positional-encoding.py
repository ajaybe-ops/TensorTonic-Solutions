import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    
    Args:
        seq_len: Length of the sequence (number of positions)
        d_model: Dimension of the model (embedding dimension)
        base: Base for the frequency calculation (default: 10000.0)
    
    Returns:
        Positional encoding matrix of shape (seq_len, d_model)
    """
    # Initialize the positional encoding matrix
    pe = np.zeros((seq_len, d_model))
    
    # Create position vector [0, 1, 2, ..., seq_len-1]
    position = np.arange(seq_len)[:, np.newaxis]  # Shape: (seq_len, 1)
    
    # Calculate the division term for frequencies
    # For even indices: use sin, for odd indices: use cos
    # The formula uses 2i/d_model for the frequency
    i = np.arange(d_model)[np.newaxis, :]  # Shape: (1, d_model)
    
    # Calculate the angle rates: 1 / (base^(2i/d_model))
    # Handle both even and odd d_model cases
    angle_rates = 1.0 / np.power(base, (2 * (i // 2)) / d_model)
    
    # Calculate the angles: position * angle_rates
    angles = position * angle_rates  # Shape: (seq_len, d_model)
    
    # Apply sin to even indices and cos to odd indices
    pe[:, 0::2] = np.sin(angles[:, 0::2])  # Even indices
    pe[:, 1::2] = np.cos(angles[:, 1::2])  # Odd indices
    
    # Handle odd d_model case: last column (index d_model-1) should be sin
    # This happens automatically because if d_model is odd, the last index is even
    # (since indices start at 0), so it will be filled with sin from the line above
    
    return pe