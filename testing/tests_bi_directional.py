
import math

INFINITY = math.inf

# Standard weighted graph (as shared by the University of Liverpool)
# graph = [[0, 7, INFINITY, 8],
#          [INFINITY, 0, 5, INFINITY],
#          [INFINITY, INFINITY, 0, 2],
#          [INFINITY, INFINITY, INFINITY, 0]]

# Graph with bi-directional and varied weights, adjusted by a factor of three
graph = [[0, 7, INFINITY, 8],
         [INFINITY, 0, 5, INFINITY],
         [INFINITY, 10, 0, 2],
         [24, INFINITY, 4, 0]]

# Number of vertices in the graph
NODE_COUNT = len(graph[0])

# Recursive implementation of Floyd-Warshall algorithm
def recursive_floyd(distances):

    def compute_shortest_path(source, target, intermediate):

        if intermediate < 0:
            return distances[source][target]

        return min(compute_shortest_path(source, target, intermediate - 1),
                   compute_shortest_path(source, intermediate, intermediate - 1)
                   + compute_shortest_path(intermediate, target, intermediate - 1))

    for intermediate in range(NODE_COUNT):
        for source in range(NODE_COUNT):
            for target in range(NODE_COUNT):
                distances[source][target] = compute_shortest_path(
                    source, target, intermediate)
    return distances

calculated_distances = recursive_floyd(graph)
print("Output for bi-directional graph with unequal weights (tripled):")
for row in calculated_distances:
    print(row)
