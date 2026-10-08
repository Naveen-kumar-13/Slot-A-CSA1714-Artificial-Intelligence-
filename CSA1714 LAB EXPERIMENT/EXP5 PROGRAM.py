moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
seen = set()

def safe(m,c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def solve(m,c,b):
    if (m,c,b) in seen:
        return False

    seen.add((m,c,b))

    if (m,c,b) == (0,0,1):
        print((m,c,b))
        return True

    for x,y in moves:
        if b == 0:
            n = (m-x,c-y,1)
        else:
            n = (m+x,c+y,0)

        if safe(n[0],n[1]) and solve(*n):
            print((m,c,b))
            return True

    return False

solve(3,3,0)
