import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
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
                break

    return G.node[b]['label']


G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()


G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()


G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()


G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()


G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
