import re

f = open("input").read().strip().split("\n")

parent_tree = {}

for line in f:
    parent = re.search(r'^[a-z]+',line).group(0)
    if not parent in parent_tree:
        parent_tree[parent] = ""
    if "->" in line:
        right = re.split(r'->',line)[1]
        nodes = re.findall(r'[a-z]+',right)
        for node in nodes:
            parent_tree[node] = parent

print(list(filter(lambda x: x[1] == "", parent_tree.items()))[0][0])
