import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

### count the length of the path between two pre-specified vertices a and b, using Depth-First-Search

def dfs(G,a,b,u):
    if a == b:
        G.add_node(b, visited = 'yes')
        G.add_node(b, label = 0)
        contOn = False

    G.add_node(a, visited = 'yes')
    G.add_node(a, label = 0)

    stack = [a]
    contOn = True
    visited = []

    while contOn == True:
        if G.node[b]['visited'] == 'yes':
            break
        x = len(stack)
        visited.append(stack[x-1])
        n = 0
        allSeen = 0

        #####################
        numberOfNeighbours = 0
        neighbors = []
        for v in G.neighbors(stack[x-1]):
            numberOfNeighbours = numberOfNeighbours + 1
            neighbors.append(v)

        neighbors.sort()
        for i in range(numberOfNeighbours):
            v = neighbors[i]
        #####################
            n = n + 1
            # if a neighbor is b finish
            if G.node[v] == G.node[b]:
                G.add_node(v, label = x)
                G.add_node(v, visited = 'yes')
                stack.append(v)
                break
            # if a neighbor is new, add to stack and continue
            elif G.node[v]['visited'] == 'no':
                G.add_node(v, visited = 'yes')
                G.add_node(v, label = x)
                stack.append(v)
                break
            # if neighbors all none or all visited move down stack
            else:
                allSeen = allSeen + 1

        if allSeen == n:
            del stack[-1]
        elif G.node[b]['visited'] == 'no':
            contOn = True
        else:
            contOn = False
            x = len(stack)
            ##################
            visited.append(stack[x-1])

    print(visited)


print()
G6=graph6.Graph()
a=12
b=40
print('Depth-First-Search visited the following nodes of G6 in this order:')
dfs(G6,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G6 between vertices', a, 'and', b, 'of length', G6.node[b]['label'])
print()


G7=graph7.Graph()
a=5
b=36
print('Depth-First-Search visited the following nodes of G7 in this order:')
dfs(G7,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G7 between vertices', a, 'and', b, 'of length', G7.node[b]['label'])
print()


G8=graph8.Graph()
a=15
b=40
print('Depth-First-Search visited the following nodes of G8 in this order:')
dfs(G8,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G8 between vertices', a, 'and', b, 'of length', G8.node[b]['label'])
print()


G9=graph9.Graph()
a=1
b=19
print('Depth-First-Search visited the following nodes of G9 in this order:')
dfs(G9,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G9 between vertices', a, 'and', b, 'of length', G9.node[b]['label'])
print()


G10=graph10.Graph()
a=6
b=30
print('Depth-First-Search visited the following nodes of G10 in this order:')
dfs(G10,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G10 between vertices', a, 'and', b, 'of length', G10.node[b]['label'])
print()
