from collections import deque

start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

q = deque([start])
visited = {start}

while q:
    s = q.popleft()

    if s == goal:
        print("Goal Reached")
        break

    z = s.index(0)
    r,c = divmod(z,3)

    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = r+dr,c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            n = nr*3+nc
            x = list(s)
            x[z],x[n] = x[n],x[z]
            x = tuple(x)

            if x not in visited:
                visited.add(x)
                q.append(x)
