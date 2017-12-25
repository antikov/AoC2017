#manual input
c = "A"
cs = 0
steps = 12481997
a = {
"A": [(1, 1, "B"),(0, -1, "C")],
"B": [(1, -1, "A"),(1, 1, "D")],
"C": [(0, -1, "B"),(0, -1, "E")],
"D": [(1, 1, "A"),(0, 1, "B")],
"E": [(1, -1, "F"),(1, -1, "C")],
"F": [(1, 1, "D"),(1, 1, "A")]
}
m = {}
for i in range(steps):
    if cs not in m: m[cs] = 0
    m[cs], step, c = a[c][m[cs]]
    cs += step
print(sum(m.values()))
