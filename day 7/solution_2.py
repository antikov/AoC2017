import re
f = open("input").read().strip().split("\n")

parent_tree = {}
tree_weight = {}
for line in f:

    parent = re.search(r'^[a-z]+',line).group(0)
    w = re.search('[0-9]+',line).group(0)
    tree_weight[parent] = int(w)

    if not parent in parent_tree:
        parent_tree[parent] = ""
    if "->" in line:
        x = re.split(r'->',line)[1]
#            print(x)
        nodes = re.findall(r'[a-z]+',x)
        for node in nodes:
#            print(line,node)
            parent_tree[node] = parent

print(parent_tree)
print(tree_weight)
def getWeight(node):
    sum = tree_weight[node]
    xxx = {}
    for x in parent_tree:
        if parent_tree[x] == node:
            xxx[x] = getWeight(x)
            sum += xxx[x]
    if len(xxx) > 0:
        xxxx = list(xxx.values())
        print(xxxx)
        for q in range(len(xxxx)):
            if (xxxx[q] != test):
                print(node, xxx)
    return sum

for h in parent_tree:
    if parent_tree[h] == "":
        initial = h
        print(h)
print(getWeight(initial))
