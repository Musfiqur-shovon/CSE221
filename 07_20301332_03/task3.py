dict = {}
file = open("input.txt", "r")
lines = file.readlines()
n = int(lines[0])

lines.pop(0)
for line in lines:
    line= line.split()
    if len(line)==1:
        dict[line[0]]=list()
    else:
        dict[line[0]]= [line[1]]
        for i in range(2,len(line)):
            dict[line[0]].append(line[i])

visited = [0] * n
printed = []

def DFS_Visit(graph, node):
    visited[int(node) - 1] = 1
    printed.append(node)
    for node in graph[node]:
        if node not in visited:
            DFS_Visit(graph, node)

def DFS(graph, endPoint):
    for node in graph:
        if node not in visited:
            DFS_Visit(graph, node)

    for i in range(len(printed)):
        print(printed[i], end=" ")
        if printed[i] == endPoint:
            break

DFS(dict, "12")