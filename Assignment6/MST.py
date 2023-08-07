def Prims(G):
    num_vertices = len(G)
    visited = [False] * num_vertices
    mst = []

    # Mark the first vertex as visited
    visited[0] = True

    while len(mst) < num_vertices - 1:
        min_weight = float('inf')
        min_edge = None

        # Find the minimum weight edge that connects a visited vertex to an unvisited vertex
        for i in range(num_vertices):
            if visited[i]:
                for j in range(num_vertices):
                    if not visited[j] and G[i][j] > 0 and G[i][j] < min_weight:
                        min_weight = G[i][j]
                        min_edge = (i, j, min_weight)

        if min_edge:
            mst.append(min_edge)
            visited[min_edge[1]] = True

    return mst
