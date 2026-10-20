def minimax(tree, depth, maximizing):
    if depth == 2:
        return tree

    values = [minimax(x, depth + 1, not maximizing) for x in tree]

    if maximizing:
        return max(values)
    return min(values)

tree = [[3, 5], [2, 9]]
print("Best Value:", minimax(tree, 0, True))
