import numpy as np

def twoGroups(n, x, p):
    if x > 2*p:
        raise ValueError('x must be less than 2p')
    group1 = network(int(n/2), x)
    group2 = network(int(n/2), x)
    y = (2*p-x)
    connect = network(int(n/2), y)
    finalNetwork1 = np.concatenate((group1, connect), axis=0)
    finalNetwork2 = np.concatenate((connect.T, group2), axis=0)
    finalNetwork = np.concatenate((finalNetwork1, finalNetwork2), axis=1)
    return finalNetwork
