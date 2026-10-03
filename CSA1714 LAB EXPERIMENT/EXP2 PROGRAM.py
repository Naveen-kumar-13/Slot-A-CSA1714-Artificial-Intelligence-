n = 8
board = [-1] * n

def safe(r,c):
    for i in range(r):
        if board[i] == c or abs(board[i]-c) == r-i:
            return False
    return True

def solve(r):
    if r == n:
        print(board)
        return True

    for c in range(n):
        if safe(r,c):
            board[r] = c
            if solve(r+1):
                return True

    return False

solve(0)
