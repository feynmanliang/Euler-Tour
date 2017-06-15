from collections import defaultdict

def find_euler_tour(graph):
    tour = []
    E = graph

    numEdges = defaultdict(int)

    def find_tour(u):
        for e in range(len(E)):
            if E[e] == 0:
                continue
            if u == E[e][0]:
                u,v = E[e]
                E[e] = 0
                find_tour(v)
            elif u == E[e][1]:
                v,u = E[e]
                E[e] = 0
                find_tour(v)
        tour.insert(0,u)

    for i,j in graph:
        numEdges[i] += 1
        numEdges[j] += 1

    start = graph[0][0]
    for i,j in numEdges.iteritems():
        if j % 2 > 0:
            start = i
            break

    current = start
    find_tour(current)

    if tour[0] != tour[-1]:
        return None
    return tour
