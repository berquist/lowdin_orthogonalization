import numpy as np


def arma_ascii_header_to_dtype(header):

    if 'IS004' in header:
        return np.int32
    else:
        return np.float64

    return dtype


def read_arma_mat_ascii(armaasciifilename):
    """Given a file name, read it in as an ASCII-formatted Armadillo matrix.

    Currently, it supports matrices and cubes.

    The second line of the file contains the dimensions:
    rows, columns, slices (not sure about fields).

    Return a NumPy ndarray of shape [nslices, nrows, ncolumns].
    """

    with open(armaasciifilename) as armafile:
        # The first line contains information about the datatype.
        header = next(armafile)
        dims = next(armafile)
        shape = [int(x) for x in dims.split()]

    dtype = arma_ascii_header_to_dtype(header)

    if len(shape) == 1:
        rows = shape[0]
        columns, slices = 1, 1
    elif len(shape) == 2:
        rows, columns = shape
        slices = 1
    elif len(shape) == 3:
        rows, columns, slices = shape
    else:
        sys.exit(1)

    arma_mat = np.loadtxt(armaasciifilename, skiprows=2, dtype=dtype)

    arma_mat = arma_mat.ravel().reshape((slices, rows, columns))

    if len(shape) == 1:
        pass
    elif len(shape) == 2:
        # Drop the cube slice dimension.
        arma_mat = arma_mat[0]
    elif len(shape) == 3:
        pass

    return arma_mat
