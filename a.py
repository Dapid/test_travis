import numpy as np

# pythran export compute_theta(int32[:, :])
def compute_theta(alignment):
    n_cols = alignment.shape[0]
    total = 0
    for i in range(n_cols):
        total += np.bincount(alignment[i, :]).sum()
    return total

