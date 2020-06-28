import numpy as np

inputMatrix = np.array([
    [5, 0, 0],
    [0, 0, 4],
    [0, 0, 6]
])

# Ik maak de vector eerst 1-dimentionaal
inputVector = inputMatrix.copy()
inputVector.resize(1, inputMatrix.size)
inputVector = np.squeeze(np.asarray(inputVector))

print(f"Matrix:\n{inputMatrix}")
print(f"\nWaardes waar wij mee gaan werken:\n{inputVector}")

# Dan maak ik de zero matrix aan
Q = np.zeros(shape=(9, 10), dtype=int)
Q[0] = [1, 1, 1, 0, 0, 0, 0, 0, 0, -1]  # Horizontaal 1
Q[1] = [0, 0, 0, 1, 1, 1, 0, 0, 0, -1]  # Horizontaal 2
Q[2] = [0, 0, 0, 0, 0, 0, 1, 1, 1, -1]  # Horizontaal 3
Q[3] = [1, 0, 0, 1, 0, 0, 1, 0, 0, -1]  # Verticaal 1
Q[4] = [1, 0, 0, 0, 1, 0, 0, 0, 1, -1]  # Diagonaal 1
Q[5] = [0, 1, 0, 0, 1, 0, 0, 1, 0, -1]  # Verticaal 2
Q[6] = [0, 0, 1, 0, 1, 0, 1, 0, 0, -1]  # Diagonaal 2
Q[7] = [0, 0, 1, 0, 0, 1, 0, 0, 1, -1]  # Verticaal 3

print(f"Matrix A:\n{Q}")
print(f"\nDe zero-vector:\n{Q.T}")  # Transposen zodat zodat de output er beter uit ziet

# Voor elke waarde in de inputvector kijken of er een waarde door de gebruiker is ingevuld.
# Verlaag de waarde in de zero vector wanneer deze al ingevuld is. De rest gaat op 0.
zeroVector = np.zeros(shape=(9, 1))
for ix, value in enumerate(inputVector):
    if value:
        for y in range(inputMatrix.size):
            if Q.T[ix][y]:
                zeroVector[y] -= value
        Q.T[:][ix] = 0

print(f"\nBijgewerkte Matrix A met shape {Q.shape}:\n{Q}")
print(f"\nBijgewerkte zero-vector met shape {zeroVector.shape}:\n{zeroVector}")

# Matrix inverse dot de zerovector en weer naar een 3x3
AInv = np.linalg.pinv(Q)
oplossingsVector = AInv @ zeroVector
oplossingsMatrix = oplossingsVector[:][:9]
oplossingsMatrix.resize(3, 3)

print(f"De oplossings-vector:\n{np.round(oplossingsVector, 3)}")
print(f"\nDe oplossing in matrix-vorm:\n{np.round(inputMatrix + oplossingsMatrix, 3)}")
