import numpy as np

def network(n, p):
    'Creates an Erdos-Renyi network, represented by a symmetrical adjacency matrix, with n nodes and p probablity that an edge between any two nodes exists.'
    matrix = np.random.rand(n, n) #Generates a matrix of dimensions n x n. We will be using the values in the upper triangle of this matrix to generate edges.
    matrix = (matrix < p).astype(np.int) #Determines the outcome of the "weighted coin flip" from the previous function: 1 or 0
    a = np.triu(matrix, 1) #Returns the upper triangle of the matrix, removing everything from the main diagonal and below.
    matrix = a + a.T #Makes the matrix symmetrical along the main diagonal. This represents an undirected network. By design, the main diagonal is composed of zeroes; a person cannot transmit a disease to themselves.
    return matrix
