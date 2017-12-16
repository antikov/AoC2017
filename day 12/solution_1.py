import re
f = open("input").read().strip().split("\n")

graph = {}
visited = [0] * 2000
for line in f:
    temp = re.split("<->",line)
    a = int(temp[0])
    b = list(map(int, temp[1].split(",")))
    graph[a] = b

print(graph,visited)
start = 0
to_visit = [start]

while len(to_visit) > 0:
    start = to_visit[0]
    del to_visit[0]
    if visited[start] == 0:
        to_visit.extend(graph[start])
        visited[start] = 1

print(sum(visited))
