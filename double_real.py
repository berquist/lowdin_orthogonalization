from __future__ import print_function

import numpy as np
np.set_printoptions(precision=4, linewidth=200, suppress=True)
import numpy.linalg as npl

from common import read_arma_mat_ascii


S = read_arma_mat_ascii("S.dat")
print("Overlap matrix")
print(S)

lam_s, l_s = npl.eigh(S)
lam_s = lam_s * np.eye(len(lam_s))
lam_sqrt_inv = np.sqrt(npl.inv(lam_s))
symm_orthog = np.dot(l_s, np.dot(lam_sqrt_inv, l_s.T))

print("Symmetric orthogonalization matrix")
print(symm_orthog)
