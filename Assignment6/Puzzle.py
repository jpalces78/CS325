def valid(Board, i, j):
    # check if board index is not outside
    return i >= 0 and j >= 0 and i < len(Board) and j < len(Board[i]) \
           and Board[i][j] == '-'


answers = []  # to store the routes


def dfs(Board, i, j, target, route):
    # if moving is not valid
    if not valid(Board, i, j):
        return
    # if we reached target
    if (i, j) == target:
        answers.append(route)
        return
    # mark current cell visited
    Board[i][j] = '#'
    # cal dfs in all four direction
    if valid(Board, i - 1, j):
        dfs(Board, i - 1, j, target, route + 'U')
    if valid(Board, i + 1, j):
        dfs(Board, i + 1, j, target, route + 'D')
    if valid(Board, i, j - 1):
        dfs(Board, i, j - 1, target, route + 'L')
    if valid(Board, i, j + 1):
        dfs(Board, i, j + 1, target, route + 'R')
    # unmark the current cell
    Board[i][j] = '-'


def solve_puzzle(Board, source, destination):
    # call the function
    dfs(Board, source[0], source[1], destination, '')
    minlen = 1e12;
    # calculate the minimum length
    for i in answers:
        minlen = min(minlen, len(i))
    actual = []
    # filter the minlen routes
    for i in answers:
        if len(i) == minlen:
            actual.append(i)
    # if there is no way
    if not len(actual):
        print(None)
        return
    # otherwise print the ans
    print(len(actual))
    print(answers[0])
