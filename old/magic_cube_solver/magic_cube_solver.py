import numpy as np
from numpy.linalg import  pinv

# Inputmatrix maken
inputMatrix = np.matrix([
    [5, None, None],
    [None, None, 4],
    [None, None, 6]
])
inputVector = inputMatrix.copy()
inputVector.resize(1,9)  # Naar vector
inputVector = np.squeeze(np.asarray(inputVector))  # Een-dimentionaal maken

print("Input matrix:\n", inputMatrix)
print("\n1D-vector:\n", inputVector)

#Zero vector bouwen
A = np.zeros(shape=(9, 10), dtype=int)
zeroVector = np.zeros(shape=(9, 1))
A[0] = [1, 1, 1, 0, 0, 0, 0, 0, 0, -1]  # Rij 1
A[1] = [0, 0, 0, 1, 1, 1, 0, 0, 0, -1]  # Rij 2
A[2] = [0, 0, 0, 0, 0, 0, 1, 1, 1, -1]  # Rij 3
A[3] = [1, 0, 0, 1, 0, 0, 1, 0, 0, -1]  # Kolom 1
A[4] = [1, 0, 0, 0, 1, 0, 0, 0, 1, -1]  # Diagonaal 1
A[5] = [0, 1, 0, 0, 1, 0, 0, 1, 0, -1]  # Kolom 2
A[6] = [0, 0, 1, 0, 1, 0, 1, 0, 0, -1]  # Diagonaal 2
A[7] = [0, 0, 1, 0, 0, 1, 0, 0, 1, -1]  # Kolom 3
A[8] = [0, 0, 0, 0, 3, 0, 0, 0, 0, -1]  # 3 * midden

position = 0
for value in inputVector:
    if value:  # Kijken of een waarde is voorgedefinieerd in de input
        for x in range(9):
            if A.T[position][x]:  # Als deze bestaat
                zeroVector[x] -= value  # Verminder de waarde in de zero-vector
        A.T[:][position] = 0  # Rijen van de vooraf ingevulde waardes zetten op 0
    position += 1  # Positie in de matrix en vector bijhouden

print("\nBijgewerkte Matrix A:\n", A)
print("\nBijgewerkte Zero-Vector:\n", zeroVector)

AInv = pinv(A)  # Pseudo-inverse
print("Matrix A geïnverteerd:\n", AInv)

solvedVector = AInv @ zeroVector  # Dot product
print("De oplossings-vector:\n", solvedVector)

position = 0
for value in inputVector:
    if value is None:
        inputVector[position] = solvedVector[position][0]
    position += 1

finalVector = np.around(inputVector.astype(np.double), 3)
finalVector.resize(3, 3)  # Vector terug naar matrix
print("De oplossings-matrix:\n", finalVector)