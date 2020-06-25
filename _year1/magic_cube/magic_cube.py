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

# Dan maak ik de zero matrix aan
zero = np.zeros(shape=(9, 10), dtype=int)
zero[0] = [1, 1, 1, 0, 0, 0, 0, 0, 0, -1]  # Horizontaal 1
zero[1] = [0, 0, 0, 1, 1, 1, 0, 0, 0, -1]  # Horizontaal 2
zero[2] = [0, 0, 0, 0, 0, 0, 1, 1, 1, -1]  # Horizontaal 3
zero[3] = [1, 0, 0, 1, 0, 0, 1, 0, 0, -1]  # Verticaal 1
zero[4] = [1, 0, 0, 0, 1, 0, 0, 0, 1, -1]  # Diagonaal 1
zero[5] = [0, 1, 0, 0, 1, 0, 0, 1, 0, -1]  # Verticaal 2
zero[6] = [0, 0, 1, 0, 1, 0, 1, 0, 0, -1]  # Diagonaal 2
zero[7] = [0, 0, 1, 0, 0, 1, 0, 0, 1, -1]  # Verticaal 3

# Voor elke waarde in de inputvector kijken of er een waarde door de gebruiker is ingevuld.
# Verlaag de waarde in de zero vector wanneer deze al ingevuld is. De rest gaat op 0.
zeroVector = np.zeros(shape=(9, 1))
for ix, value in enumerate(inputVector):
    if value:
        for y in range(inputMatrix.size):
            if zero.T[ix][y]:
                zeroVector[y] -= value
        zero.T[:][ix] = 0

# Matrix inverse dot de zerovector en weer naar een 3x3
AInv = np.linalg.pinv(zero)
oplossingsVector = AInv @ zeroVector
oplossingsMatrix = oplossingsVector[:][:9]
oplossingsMatrix.resize(3, 3)

print(inputMatrix + oplossingsMatrix)
