cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
path = [0]
total = 0

while len(path) < n:
    last = path[-1]
    next_city = -1
    minimum = float('inf')

    for i in range(n):
        if i not in path and cost[last][i] < minimum:
            minimum = cost[last][i]
            next_city = i

    path.append(next_city)
    total += minimum

total += cost[path[-1]][path[0]]
path.append(path[0])

print("Path:", path)
print("Total Distance:", total)
