
import sys
import math
from queue import PriorityQueue

def dijktra(Graph, source):

    dist = [math.inf] * len(Graph)
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
            for x in G[u]:
                v = x[0]
                alt = dist[u - 1] + x[1]
                if alt < dist[v - 1]:
                    dist[v - 1] = alt
                    prev[v - 1] = u
                    Q.put((dist[v - 1], v))


    if len(prev) == 1:
        print(1)
    else:
        a = prev[-1]
        array = [len(prev)]
        while True:
            if a is None:
                break
            else:
                array.append(a)
                a = prev[a - 1]
        array.reverse()
        for x in array:
            print(x, end=" ")
        print()


sys.stdin = open("input2.txt", "r")
sys.stdout = open("output2.txt", "w")

inputs = open("input1.txt", "r").readlines()

caseNo = int(input())

cases = []
routs = []

for i in range(1, len(inputs)):
    a = inputs[i].split()
    if len(a) == 2:
        cases.append(a)
    else:
        routs.append(a)
for i in cases:
    graph = {}
    for j in range(int(i[1])):
        edges = []
        val = list(map(int, routs.pop(0)))
        if val[0] in graph.keys():
            edges = graph[val[0]]
        edges.append(val[1:])
        graph[val[0]] = edges
    for k in range(1, int(i[0]) + 1):
        if k not in graph:
            graph[k] = None
    graph = {u: v for u, v in sorted(graph.items())}
    dijktra(graph, 1)