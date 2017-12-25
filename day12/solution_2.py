import re
f = open("input").read().strip().split("\n")

graph = {}
visited = [0] * 2000
for line in f:
    temp = re.split("<->",line)
    a = int(temp[0])
    b = list(map(int, temp[1].split(",")))
    graph[a] = b

group = 0

while (sum(visited) < len(visited)):
    for i in range(len(visited)):
        if visited[i] == 0:
            start = i
            to_visit = [start]
            group += 1

            while len(to_visit) > 0:
                start = to_visit[0]
                del to_visit[0]
                if visited[start] == 0:
                    to_visit.extend(graph[start])
                    visited[start] = group

print(max(visited))
