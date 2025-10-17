"""
Load observational data
"""

import numpy as np

def load_observational_data(filepath):
    """
    Load observational data from text file.
    
    Args:
        filepath: Path to the data file
    
    Returns:
        Tuple of (k, P(k), error) arrays or (None, None, None) if loading fails
    """
    try:
        k, Pk, σPk = np.loadtxt(filepath).T
        print(f"Loaded observational data: {len(k)} points")
        print(f"  k range: [{k.min():.2e}, {k.max():.2e}] h/Mpc")
        return k, Pk, σPk
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None, None