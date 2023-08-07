from collections import deque

def is_valid_move(board, row, col):
    # Check if the move is within the bounds of the board and is an empty cell
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '-'

def get_direction(prev_row, prev_col, new_row, new_col):
    if new_row == prev_row - 1:
        return 'U'
    elif new_row == prev_row + 1:
        return 'D'
    elif new_col == prev_col - 1:
        return 'L'
    elif new_col == prev_col + 1:
        return 'R'
    else:
        return ''

def solve_puzzle(board, source, destination):
    if source == destination:
        return [source], ''

    queue = deque()
    queue.append([source])

    visited = set()
    visited.add(source)

    while queue:
        path = queue.popleft()
        row, col = path[-1]

        if (row, col) == destination:
            # Build directions only for the correct path
            directions = ''
            for i in range(1, len(path)):
                directions += get_direction(path[i-1][0], path[i-1][1], path[i][0], path[i][1])
            return path, directions

        # Check possible moves: left, right, up, down
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(board, new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                new_path = list(path)
                new_path.append((new_row, new_col))
                queue.append(new_path)

    # If no path is found
    return None, ''

# Example usage
board = [ ['-', '-', '-', '-', '-'], ['-', '-', '#', '-', '-'], ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-'], ['-', '#', '-', '-', '-'] ]
source = (0, 0)
destination = (2, 2)
path, directions = solve_puzzle(board, source, destination)
print("Path:", path)
print("Directions:", directions)
