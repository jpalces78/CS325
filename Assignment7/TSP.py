def solve_tsp(G):
    num_nodes = len(G)
    visited = [False] * num_nodes
    path = []

    current_node = 0  # Starting from node 0
    path.append(current_node)
    visited[current_node] = True

    while len(path) < num_nodes:
        next_node = None
        min_distance = float('inf')

        for neighbor in range(num_nodes):
            if not visited[neighbor] and G[current_node][neighbor] > 0 and G[current_node][neighbor] < min_distance:
                next_node = neighbor
                min_distance = G[current_node][neighbor]

        if next_node is None:
            break

        path.append(next_node)
        visited[next_node] = True
        current_node = next_node

    # Return to starting node
    path.append(0)

    return path

# Sample input
G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]

# Get the TSP path using the nearest-neighbor heuristic
tsp_path = solve_tsp(G)
print(tsp_path)

