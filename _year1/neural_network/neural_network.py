import numpy as np
import json

def matrix_vector_product(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    new_vector = np.ndarray(v.shape)
    for i,x in enumerate(M.T):
        number = 0
        for y in x:
            number+=y*v[i]
        new_vector[i] = number
    return new_vector

def matrix_product(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    result = np.zeros(shape=X.shape)
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def read_layer(data, json_index) -> np.ndarray:
    size_in = int(data[json_index]['size_in'])
    size_out = int(data[json_index]['size_out'])
    matrix = np.zeros([size_in, size_out])
    for x in data[json_index]['weights']:
        for y in data[json_index]['weights'][x]:
            matrix[int(x) - 1][int(y) - 1] = data[json_index]['weights'][x][y]
    return matrix


def read_network(filename: str) -> np.ndarray:
    with open(filename) as json_file:
        data = json.load(json_file)

        if filename == 'example.json':
            return read_layer(data, 'layer1')
        if data['layer1']:
            matrix1 = read_layer(data, 'layer1')
        if filename == 'example-2layer.json':
            matrix2 = read_layer(data, 'layer2')
    return np.dot(matrix1, matrix2)
    # return matrix_product(matrix1, matrix2)


def run_network(filename: str, input_vector: np.ndarray) -> np.ndarray:
    matrix = read_network(filename)
    # return matrix.T.dot(input_vector)
    return matrix_vector_product(matrix, input_vector)

# print(read_network("example-2layer.json"))
print(run_network("example.json", np.array([1, 1, 1, 1, 1])))
print(run_network("example-2layer.json", np.array([1, 1, 1, 1, 1])))
