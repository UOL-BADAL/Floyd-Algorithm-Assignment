import math
import itertools
import tracemalloc

INFINITY = math.inf

# Graph setup provided by the University of Liverpool
graph = [[0, 7, INFINITY, 8],
         [INFINITY, 0, 5, INFINITY],
         [INFINITY, INFINITY, 0, 2],
         [INFINITY, INFINITY, INFINITY, 0]]

# Determine the number of nodes based on the provided graph
TOTAL_NODES = len(graph[0])

# Imperative implementation of Floyd's algorithm, as assigned
def imperative_floyd(distances):

    distances = list(map(lambda node: list(map(lambda edge: edge, node)), distances))

    for intermediary in range(TOTAL_NODES):
        for source in range(TOTAL_NODES):
            for target in range(TOTAL_NODES):
                distances[source][target] = min(
                    distances[source][target],
                    distances[source][intermediary] + distances[intermediary][target])
    return distances

# Recursive method for Floyd's algorithm
def recursive_floyd(distances):

    def find_path(source, target, step):

        if step < 0:
            return distances[source][target]

        return min(find_path(source, target, step - 1),
                   find_path(source, step, step - 1) + find_path(step, target, step - 1))

    for step in range(TOTAL_NODES):
        for source in range(TOTAL_NODES):
            for target in range(TOTAL_NODES):
                distances[source][target] = find_path(source, target, step)
    return distances

# Itertools-based implementation of Floyd's algorithm
def itertools_floyd(distances):

    for intermediary, source, target in itertools.product(range(TOTAL_NODES), repeat=3):

        if source == target:
            distances[source][target] = 0
            continue

        distances[source][target] = min(distances[source][target],
                                        distances[source][intermediary] + distances[intermediary][target])
    return distances

def check_memory_usage():
    """Evaluate current and peak memory usage across different implementations of Floyd's algorithm."""

    # Monitoring memory for the imperative version
    tracemalloc.start()
    imperative_floyd(graph)
    current_mem_imp, peak_mem_imp = tracemalloc.get_traced_memory()
    print("Memory footprint for imperative Floyd's algorithm:")
    print(f"Current memory usage: {current_mem_imp}")
    print(f"Peak memory usage: {peak_mem_imp}")
    tracemalloc.stop()

    # Monitoring memory for the recursive version
    tracemalloc.start()
    recursive_floyd(graph)
    current_mem_rec, peak_mem_rec = tracemalloc.get_traced_memory()
    print("\nMemory footprint for recursive Floyd's algorithm:")
    print(f"Current memory usage: {current_mem_rec}")
    print(f"Peak memory usage: {peak_mem_rec}")
    tracemalloc.stop()

    # Monitoring memory for the itertools version
    tracemalloc.start()
    itertools_floyd(graph)
    current_mem_itertools, peak_mem_itertools = tracemalloc.get_traced_memory()
    print("\nMemory footprint for itertools Floyd's algorithm:")
    print(f"Current memory usage: {current_mem_itertools}")
    print(f"Peak memory usage: {peak_mem_itertools}")
    tracemalloc.stop()

check_memory_usage()

