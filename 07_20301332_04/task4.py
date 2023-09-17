
import sys
import math
from queue import PriorityQueue

def Network(Graph, source):

    dist = [-1] * len(Graph)
    dist[source - 1] = 0

    visited = [False] * len(Graph)
    prev = [None] * len(Graph)

    Q = PriorityQueue()
    Q.put((dist[source - 1], source))

    while Q.empty() is False:
        u = Q.get()[1]
        if visited[u - 1]:
            continue
        visited[u - 1] = True
        if Graph[u] is not None:
            for x in Graph[u]:
                v = x[0]
                alt = dist[u - 1] + x[1]
                if dist[u] > x[1]:
                    alt = x[1]
                else:
                    alt = dist[u - 1] + x[1]
                if alt > dist[v - 1]:
                    dist[v - 1] = alt
                    prev[v - 1] = u
                    Q.put((dist[v - 1], v))


    if len(dist) != 1:
        array = dist[1:]
        array.sort()
        x = array[0]
        dist[-1] = x

    for v in dist:
        print(v, end=" ")

    print()




sys.stdin = open("input4.txt", "r")
sys.stdout = open("output4.txt", "w")

inputs = open("input4.txt", "r").readlines()

caseNo = int(input())

sources = []
connections = []
routs = []

for i in range(1, len(inputs)):
    a = inputs[i].split()
    if len(a) == 1:
        sources.append(a)
    elif len(a) == 2:
        connections.append(a)
    elif len(a) == 3:
        routs.append(a)

for i in connections:
    source = int(sources.pop(0)[0])
    graph = {}
    for j in range(int(i[1])):
        edges = []
        val = list(map(int, routs.pop(0)))
        if val[0] in graph.keys():
            edges = graph[(val[0])]
        edges.append(val[1:])
        graph[val[0]] = edges




    for k in range(1, int(i[0]) + 1):
        if k not in graph:
            graph[k] = None


    graph = {u: v for u, v in sorted(graph.items())}
    Network(graph, source)