import numpy as np
import json

def read_layer(data, json_index) -> np.ndarray:
    size_in = int(data[json_index]['size_in'])
    size_out = int(data[json_index]['size_out'])
    weights = data[json_index]['weights']
    matrix = np.zeros([size_in, size_out])
    for x in data[json_index]['weights']:
        for y in data[json_index]['weights'][x]:
            matrix[int(x) - 1][int(y) - 1] = data[json_index]['weights'][x][y]
    return matrix

def read_network(filename: str) -> np.ndarray:
    with open(filename) as json_file:
        data = json.load(json_file)
        if data['layer1']:
            matrix1 = read_layer(data, 'layer1')
        if filename=='example-2layer.json':
            matrix2 = read_layer(data, 'layer2')
    return np.dot(matrix1, matrix2)

def run_network(filename: str, input_vector: np.ndarray) -> np.ndarray:
    matrix = read_network(filename)
    return matrix.T.dot(input_vector)

# print(read_network("example-2layer.json"))
matrix = run_network("example-2layer.json", np.array([1,1,1,1,1]))
print(matrix)




#
# x = np.array([1, 1, 1, 1, 1])
# layer1 = np.array([
#     [0.5, 0.2, 0, -0.1],
#     [0.2, -0.5, -0.2, 0.8],
#     [0, -0.1, 0, 0.3],
#     [0, 0.9, 0.1, 0],
#     [-0.2, -0.8, -0.1, -0.7]
# ])
#
# a = x.dot(layer1)
# print(a)
