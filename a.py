import numpy as np

# pythran export compute_theta(int8[:, :])
def compute_theta(alignment):
    alignment_depth = alignment.shape[1]
    total = 0
    for i in range(n_cols):
        total += np.bincount(alignment[i, :]).sum()
    return total

