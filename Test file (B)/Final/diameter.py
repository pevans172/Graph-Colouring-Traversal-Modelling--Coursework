import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10

# modified bfs to use for just spanning out across whole tree the shortest path
def bfs(G,a):
    if len(G.nodes()) == 0:
        return 0
    queue = []
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    layer = 0
    G.add_node(a, label = layer)
    queue.append(a)
    checkList = []
    nodesLeft = True

    while nodesLeft == True:
        layer = layer+1
        length = len(queue)
        for i in range(length):
            for x in nx.all_neighbors(G, queue[i]):
                if G.node[x]['label'] == -1:
                    G.add_node(x, label = layer)
                    queue.append(x)

        for j in range(length):
            del queue[0]

        nodesLeft = False
        for v in G.nodes():
            if G.node[v]['label'] == -1:
                nodesLeft = True

    return layer
    


def max_distance(G):
    layer = 0
    temp = 0
    for v in G.nodes():
        temp = bfs(G,v)
        if temp > layer:
            layer = temp
    return layer


print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()
