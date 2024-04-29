
import math

INFINITE = math.inf

# Experiment to determine the effect of non-zero initial values at nodes on the computation

# Baseline graph with zero-initialized nodes
# graph = [[0, 7, INFINITE, 8],
#          [INFINITE, 0, 5, INFINITE],
#          [INFINITE, INFINITE, 0, 2],
#          [INFINITE, INFINITE, INFINITE, 0]]

# First node's initial value set to non-zero
# graph = [[3, 7, INFINITE, 8],
#          [INFINITE, 0, 5, INFINITE],
#          [INFINITE, INFINITE, 0, 2],
#          [INFINITE, INFINITE, INFINITE, 0]]

# Second node's initial value set to non-zero
# graph = [[3, 7, INFINITE, 8],
#          [INFINITE, 4, 5, INFINITE],
#          [INFINITE, INFINITE, 0, 2],
#          [INFINITE, INFINITE, INFINITE, 0]]

# Third node's initial value adjusted to non-zero
# graph = [[3, 7, INFINITE, 8],
#          [INFINITE, 4, 5, INFINITE],
#          [INFINITE, INFINITE, 5, 2],
#          [INFINITE, INFINITE, INFINITE, 0]]

# Fourth node's initial value modified to non-zero
graph = [[3, 7, INFINITE, 8],
         [INFINITE, 4, 5, INFINITE],
         [INFINITE, INFINITE, 5, 2],
         [INFINITE, INFINITE, INFINITE, 6]]

NUMBER_OF_NODES = len(graph[0])

def recursive_floyd(distances):

    def calculate_min_path(src, dest, intermediate):

        if intermediate < 0:
            return distances[src][dest]

        return min(calculate_min_path(src, dest, intermediate - 1),
                   calculate_min_path(src, intermediate, intermediate - 1)
                   + calculate_min_path(intermediate, dest, intermediate - 1))

    for intermediate in range(NUMBER_OF_NODES):
        for src in range(NUMBER_OF_NODES):
            for dest in range(NUMBER_OF_NODES):
                distances[src][dest] = calculate_min_path(
                    src, dest, intermediate)
    return distances

updated_distances = recursive_floyd(graph)
print("Output with a non-zero value in the fourth node:")
for row in updated_distances:
    print(row)
