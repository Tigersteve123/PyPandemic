import random
import matplolib.pyplot as plt

def infect(a, b, p):
    if a['status'] == 'infected' and b['status'] == 'healthy':
        if random.random() < p:
            b['status'] = 'infected'
    return b

def countStatus(nodes, status):
    return sum([1 if x['status'] == status else 0 for x in nodes])

def graph(total, infected, removed):
    x = range(len(removed))
    plt.fill_between(x, infected, removed, color='#1f77b4', label='susceptible') #susceptible
    plt.fill_between(x, 0, infected, color='#ff7f0e', label='infected') #infected
    plt.fill_between(x, removed, total, color='#2ca02c', label='removed') #removed
    plt.xlabel('Periods')
    plt.ylabel('Nodes')
    plt.legend()
    plt.show()

def disease(network, p, r, returnGraph=True):
    n = len(network) #number of nodes
    nodes = [None for x in range(n)] #initializes the list of nodes
    for i in range(n):
        nodes[i] = {'id': i, 'status': 'healthy', 'infectedTime': 0, 'connected': []} #initializes all nodes as 'healthy'
  
    #Generates a list of all connected nodes for each node
    for i in range(n):
        for j in range(n):
            if network[i, j] == 1:
                nodes[i]['connected'].append(j)
                nodes[j]['connected'].append(i)

    patientZeroID = random.randint(0, n-1) #Chooses a node at random to start the infection
    nodes[patientZeroID]['status'] = 'infected' #Changes the status of the node to 'infected'
    countInfected = countStatus(nodes, 'infected')

    total = n

    infected = []
    removed = []

    while countInfected != 0:
        nodesBeg = nodes
        for i in range(n):
            if nodesBeg[i]['status'] == 'infected':
                for j in nodes[i]['connected']:
                    nodes[j] = infect(nodesBeg[i], nodesBeg[j], p)
        for i in nodes:
            if i['infectedTime'] >= r:
                i['status'] = 'recovered'
            if i['status'] == 'infected':
                i['infectedTime'] += 1
        countInfected = countStatus(nodes, 'infected')
        infected.append(countInfected)
        removed.append(total - countStatus(nodes, 'recovered'))

    peak = max(infected)
    peakTime = infected.index(max(infected))
    totalTime = len(infected)
    totalInfected = countStatus(nodes, 'recovered')

    #Graph
    if returnGraph:
        graph(total, infected, removed)

    return peak, peakTime, totalTime, totalInfected
