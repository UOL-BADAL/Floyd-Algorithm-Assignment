
import math

# Different definitions for the representation of no direct path
# MAX_DISTANCE = math.inf
MAX_DISTANCE = 13

graph = [[0, 7, MAX_DISTANCE, 8],
         [MAX_DISTANCE, 0, 5, MAX_DISTANCE],
         [MAX_DISTANCE, MAX_DISTANCE, 0, 2],
         [MAX_DISTANCE, MAX_DISTANCE, MAX_DISTANCE, 0]]

NODE_COUNT = len(graph[0])


def recursive_floyd(dist_matrix):

    def compute_min_distance(source, target, intermediate):

        if intermediate < 0:
            return dist_matrix[source][target]

        return min(compute_min_distance(source, target, intermediate - 1),
                   compute_min_distance(source, intermediate, intermediate - 1)
                   + compute_min_distance(intermediate, target, intermediate - 1))

    for step in range(NODE_COUNT):
        for src in range(NODE_COUNT):
            for dest in range(NODE_COUNT):
                dist_matrix[src][dest] = compute_min_distance(
                    src, dest, step)
    return dist_matrix


# Examples for testing the effect of using different non-infinite max values

# Display initial state of the graph matrix
# print("Initial graph matrix:")
# for row in graph:
#     print(row)

# Display the correctly calculated shortest paths
# calculated_result = recursive_floyd(graph)
# print("Expected correct output:")
# for row in calculated_result:
#     print(row)

# Demonstrate the result when MAX_DISTANCE is set below the largest required path value.
# Here, setting MAX_DISTANCE = 11 results in an incorrect solution since the actual 
# longest path required might be 12.
calculated_result = recursive_floyd(graph)
print("Output showing incorrect paths:")
for row in calculated_result:
    print(row)
