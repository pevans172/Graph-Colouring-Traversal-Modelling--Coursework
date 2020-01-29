import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    n = len(G.nodes())
    nodeNumber = 0
    checker = False
    for i in range(2, n+1):
        if G.node[i]['color'] == 0:
            for x in nx.all_neighbors(G, i):
                # the color value
                c = G.node[x]['color']
                # means no color
                if c != 0:
                    checker = True
                    break
        if checker == True:
            nodeNumber = i
            break
            
    return nodeNumber

def find_smallest_color(G,v):
    n = len(G.nodes())
    global kmax
    # gets all the possible number colours
    validColors = []
    for i in range(kmax):
        x = i+1
        validColors.append(x)

    # gets a list all the neighbours and their colours
    connected = []
    for i in nx.all_neighbors(G, v):
        # the color value
        c = G.node[i]['color']
        # means no color
        if c == 0:
            continue
        # get rid of duplicate entries
        unique = True
        for x in connected:
            if c == x:
                unique = False
                break
        if unique == True:
            connected.append(c)

    # go through this list and remove the elements from validcolors
    for i in connected:
        validColors.remove(i)
    # find the smallest value left and if there isnt one then take it as kmax+1
    if validColors != []:
        return validColors[0]
    else:
        return kmax+1

def greedy(G):
    n = len(G.nodes())
    global visited_counter
    global kmax
    kmax = 0
    if len(G.nodes()) != 0:
        kmax = 1
        # if colour is 0 its not visited
        G.add_nodes_from(G.nodes(), color = 0)
        # start at vector 1
        G.add_node(1, color = 1)
        # start going through and getting colors
        for i in range(2, n+1):
            v = find_next_vertex(G)
            x = find_smallest_color(G,v)
            G.add_node(v, color = x)
            if x > kmax:
                kmax = x
    # move on to give output
    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()


print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
