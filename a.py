import numpy as np

#pythran export compute(int8[:])
def compute(vector):
   return np.bincount(vector)


