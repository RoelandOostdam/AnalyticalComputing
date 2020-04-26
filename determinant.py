import numpy as np


def determinant_2(M: np.ndarray) -> int:
    if M.shape != (2, 2):
        raise ValueError
    return (M[0, 0] * M[1, 1]) - (M[1, 0] * M[0, 1])


def determinant_3(M: np.ndarray) -> int:  # TODO
    a = M[0, 0] * M[1, 1] * M[2, 2]
    b = M[1, 0] * M[2, 1] * M[0, 2]
    c = M[2, 0] * M[0, 1] * M[1, 2]
    d = M[2, 0] * M[1, 1] * M[0, 2]
    e = M[1, 0] * M[0, 1] * M[2, 0]
    f = M[0, 0] * M[2, 1] * M[1, 2]
    uitkomst = a + b + c - d - e -f
    return uitkomst


def determinant(M: np.ndarray) -> int:  # TODO
    pass


arr = np.array(
    [
        [1, 1, 0],
        [0, 3, 4],
        [1, 2, 1]
    ]
)
print(determinant_3(arr))
