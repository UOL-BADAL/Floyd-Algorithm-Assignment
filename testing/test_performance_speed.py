import math
import itertools
import time

UNBOUNDED = math.inf

matrix = [[0, 7, UNBOUNDED, 8],
          [UNBOUNDED, 0, 5, UNBOUNDED],
          [UNBOUNDED, UNBOUNDED, 0, 2],
          [UNBOUNDED, UNBOUNDED, UNBOUNDED, 0]]

TOTAL_NODES = len(matrix[0])


def floyd_warshall_imperative(distances):

    # Copy the matrix to preserve input data
    distances = list(map(lambda node: list(map(lambda edge: edge, node)), distances))

    # Compute shortest paths using a nested loop structure
    for k in range(TOTAL_NODES):
        for i in range(TOTAL_NODES):
            for j in range(TOTAL_NODES):
                distances[i][j] = min(
                    distances[i][j],
                    distances[i][k] + distances[k][j])
    return distances


def floyd_warshall_recursive(distances):

    def compute_path(i, j, k):

        if k < 0:
            return distances[i][j]

        return min(compute_path(i, j, k - 1),
                   compute_path(i, k, k - 1) + compute_path(k, j, k - 1))

    # Apply recursive computation to all node pairs
    for k in range(TOTAL_NODES):
        for i in range(TOTAL_NODES):
            for j in range(TOTAL_NODES):
                distances[i][j] = compute_path(i, j, k)
    return distances


def floyd_warshall_itertools(distances):

    # Use itertools.product for a cleaner triple loop
    for k, i, j in itertools.product(range(TOTAL_NODES), repeat=3):

        # Direct path override when i == j
        if i == j:
            distances[i][j] = 0
            continue

        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances


def evaluate_performance():

    # Evaluate average execution time for each Floyd-Warshall implementation over 15,000 iterations
    iterations = 15000

    start_time = time.time()
    for _ in range(iterations):
        floyd_warshall_imperative(matrix)
    imperative_duration = time.time() - start_time

    start_time = time.time()
    for _ in range(iterations):
        floyd_warshall_recursive(matrix)
    recursive_duration = time.time() - start_time

    start_time = time.time()
    for _ in range(iterations):
        floyd_warshall_itertools(matrix)
    itertools_duration = time.time() - start_time

    return (imperative_duration, recursive_duration, itertools_duration)


# Gather performance metrics
imperative_speed, recursive_speed, itertools_speed = evaluate_performance()

# Format and display results
formatted_imperative = round(imperative_speed, 3)
formatted_recursive = round(recursive_speed, 3)
formatted_itertools = round(itertools_speed, 3)

# Output formatted performance data
print(f"Imperative Method Performance: {formatted_imperative}s")
print(f"Recursive Method Performance: {formatted_recursive}s")
print(f"Itertools Method Performance: {formatted_itertools}s")
