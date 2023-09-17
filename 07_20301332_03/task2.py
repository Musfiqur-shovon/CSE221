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
queue = []
def BFS(visited, graph, node, endPoint):
    visited[int(node) - 1] = 1
    queue.append(node)
    while queue is not None:
        m = queue.pop(0)
        print(m,end=" ")
        if m == endPoint:
            break
        for neighbour in graph[m]:
            if visited[int(neighbour) - 1] == 0:
                visited[int(neighbour) - 1] = 1
                queue.append(neighbour)

BFS(visited, dict, "1", "12")