import math

INF = math.inf

# An example graph provided by the university of Liverpool
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]


# Determine the number of vertices based on the input graph
VERTEX_COUNT = len(graph[0])


def recursive_floyd(distances):
    """This function demonstrates the implementation of the Floyd-Warshall algorithm
    using recursion to find the shortest paths between all pairs of nodes."""

    # Recursive function to compute the shortest path considering all intermediate nodes
    def find_minimum_path(origin, destination, intermediate):
        # Base case: no more intermediate nodes to consider
        if intermediate < 0:
            return distances[origin][destination]

        # Recursive case: calculate the minimum path using the current intermediate node
        return min(find_minimum_path(origin, destination, intermediate - 1),
                   find_minimum_path(origin, intermediate, intermediate - 1)
                   + find_minimum_path(intermediate, destination, intermediate - 1))

    # Update the matrix with the shortest paths found
    for k in range(VERTEX_COUNT):
        for i in range(VERTEX_COUNT):
            for j in range(VERTEX_COUNT):
                distances[i][j] = find_minimum_path(i, j, k)
    return distances


# Execute Floyd-Warshall recursively and capture the output
calculated_paths = recursive_floyd(graph)

# Output the shortest paths
print("Computed shortest paths:")
for row in calculated_paths:
    print(row)
