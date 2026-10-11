from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
q = deque(['A'])
visited = []
while q:
    node = q.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        q.extend(graph[node])
