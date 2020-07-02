import numpy as np
import json


def matrix_vector_product(M: np.ndarray, v: np.ndarray, size_out) -> np.ndarray:
    """
    Deze functie voert een matrix-vector product uit
    :param M: Matrix
    :param v: Vector
    :param size_out: Output grootte
    :return: vector als ndarray
    """
    new_vector = np.ndarray((size_out, 1))  # Maak een lege vector
    for i, x in enumerate(M.T):  # Voor elke index in de matrix
        if i >= size_out:  # Respecteer vector output size
            break
        number = 0  # Begin vanaf 0
        for y in x:  # Voor elk column in de row
            number += y * v[i]  # Value multipliceren met vector
        new_vector[i] = number  # Waarde toevoegen aan vector
    return new_vector.T  # Return de transposed ndarray als vector


def matrix_product(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Deze functie voert een matrix-matrix multiplicatie uit
    :param X: Matrix 1
    :param Y: Matrix 2
    :return: Matrix als ndarray
    """
    result = np.zeros(shape=X.shape)
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def read_layer(data, json_index):
    """
    Deze functie leest een json netwerk bestand
    :param data: json.load
    :param json_index: layer index om te laden (slechte json opbouw zorgt hiervoor)
    :return: Matrix, output vector grootte
    """
    size_in = int(data[json_index]['size_in'])
    size_out = int(data[json_index]['size_out'])
    matrix = np.zeros([size_in, size_out])
    for x in data[json_index]['weights']:
        for y in data[json_index]['weights'][x]:
            matrix[int(x) - 1][int(y) - 1] = data[json_index]['weights'][x][y]
    return matrix, size_out


def read_network(filename: str):
    with open(filename) as json_file:
        data = json.load(json_file)

        if filename == 'example.json':
            matrix, output_vector = read_layer(data, 'layer1')
            return matrix, output_vector
        if data['layer1']:
            matrix1, output_vector = read_layer(data, 'layer1')
        if filename == 'example-2layer.json':
            matrix2, output_vector = read_layer(data, 'layer2')
    # return np.dot(matrix1, matrix2)
    return matrix_product(matrix1, matrix2), output_vector


def run_network(filename: str, input_vector: np.ndarray) -> np.ndarray:
    """
    Draait het netwerk en geeft de output vector terug
    :param filename: json input bestand
    :param input_vector: input vector
    :return: Output vector
    """
    matrix, size_out = read_network(filename)
    # return matrix.T.dot(input_vector)
    return matrix_vector_product(matrix, input_vector, size_out)


#  Driver Code
print(run_network("example.json", np.array([1, 1, 1, 1, 1])))  # Single layer network
print(run_network("example-2layer.json", np.array([1, 1, 1, 1, 1])))  # Double layer network
