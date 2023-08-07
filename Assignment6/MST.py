def Prims(G):
    """
    Input:
    G: The input graph represented as a square matrix (list of lists). G[i][j] represents the weight of the edge between
    vertices i and j. If there is no edge between vertices i and j, the value of G[i][j] should be 0 or a special marker
    representing infinity.
    Output:
    The function returns the Minimum Spanning Tree (MST) of the input graph as a list of edges.
    Each edge is represented as a tuple (u, v, weight) where u and v are the vertices connected by the edge, and weight
    is the weight of that edge. The MST is constructed by selecting the minimum-weight edges that connect all the
    vertices in the graph without forming any cycles.
    """
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


