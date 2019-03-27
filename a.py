import numpy as np

# pythran export compute_theta(int8[:, :])
def compute_theta(alignment):
    alignment_depth = alignment.shape[1]
    n_cols = alignment.shape[0]

    meanfracid = 0.0
    for i in range(n_cols):
        match_groups = np.bincount(alignment[i, :])
        # N choose 2 has a nice polynomial expansion:
        meanfracid += np.sum(match_groups * (match_groups - 1) / 2)
    meanfracid /= (0.5 * alignment_depth * (alignment_depth - 1) * n_cols)
    theta = min(0.5, 0.38 * 0.32 / meanfracid)
    return theta

