
import math

UNLIMITED = math.inf

# Example of a graph with positive weights
# graph = [[0, 7, UNLIMITED, 8],
#          [UNLIMITED, 0, 5, UNLIMITED],
#          [UNLIMITED, UNLIMITED, 0, 2],
#          [UNLIMITED, UNLIMITED, UNLIMITED, 0]]

# Example of a graph with a negative weight
# graph = [[0, 7, UNLIMITED, 8],
#          [UNLIMITED, 0, -5, UNLIMITED],
#          [UNLIMITED, UNLIMITED, 0, 2],
#          [UNLIMITED, UNLIMITED, UNLIMITED, 0]]

# Example of a graph containing a negative cycle
graph = [[0, -7, UNLIMITED, 8],
         [UNLIMITED, 0, -5, UNLIMITED],
         [UNLIMITED, UNLIMITED, 0, 2],
         [UNLIMITED, UNLIMITED, UNLIMITED, 0]]

TOTAL_NODES = len(graph[0])


def recursive_floyd(distances):

    def find_path(source, destination, intermediate):

        if intermediate < 0:
            return distances[source][destination]

        return min(find_path(source, destination, intermediate - 1),
                   find_path(source, intermediate, intermediate - 1)
                   + find_path(intermediate, destination, intermediate - 1))

    for intermediate in range(TOTAL_NODES):
        for source in range(TOTAL_NODES):
            for destination in range(TOTAL_NODES):
                distances[source][destination] = find_path(
                    source, destination, intermediate)
    return distances


# Example outputs before and after computation for various graph types

# Print the state of a positive weighted graph before computations
# print("Initial state of a positively weighted graph:")
# for row in graph:
#     print(row)

# Resulting state after applying Floyd's recursive method
# updated_graph = recursive_floyd(graph)
# print("Updated state of a positively weighted graph:")
# for row in updated_graph:
#     print(row)

# Print the state of a graph with negative weights before computations
# print("Initial state of a negatively weighted graph:")
# for row in graph:
#     print(row)

# Resulting state after applying Floyd's recursive method
# updated_graph = recursive_floyd(graph)
# print("Updated state of a negatively weighted graph:")
# for row in updated_graph:
#     print(row)

# Display a graph that has a negative cycle before any calculations
# updated_graph = recursive_floyd(graph)
# print("Graph state with a negative cycle:")
# for row in updated_graph:
#     print(row)

# Final output showing an incorrect result due to a negative cycle
updated_graph = recursive_floyd(graph)
print("Incorrect output due to a negative cycle:")
for row in updated_graph:
    print(row)

