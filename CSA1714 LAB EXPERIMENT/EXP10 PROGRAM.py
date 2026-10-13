graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 5, 'B': 4, 'C': 1, 'D': 0}
open_list = [('A', 0)]
cost = {'A': 0}
parent = {'A': None}

while open_list:
    open_list.sort(key=lambda x: x[1] + h[x[0]])
    node, _ = open_list.pop(0)

    if node == 'D':
        break

    for nxt, w in graph[node]:
        new = cost[node] + w

        if nxt not in cost or new < cost[nxt]:
            cost[nxt] = new
            parent[nxt] = node
            open_list.append((nxt, new))

path = []
node = 'D'

while node is not None:
    path.append(node)
    node = parent[node]

print("Path:", path[::-1])
print("Cost:", cost['D'])
