from collections import defaultdict

def find_euler_tour(graph):
    tour = []
    E = graph

    numEdges = defaultdict(int)

    def find_tour(u):
        for e in E:
            if u == e[0]:
                u,v = e
                E.remove(e)
                find_tour(v)
            elif u == e[1]:
                v,u = e
                E.remove(e)
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

    return tour

print find_euler_tour([(1,2),(2,3),(3,1)])
print find_euler_tour([(1,3),(1,5),(3,4),(3,2),(5,2),(2,4)])
print find_euler_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
