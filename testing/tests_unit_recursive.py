
import unittest
from floyd_algorithms import recursive_floyd
INFINITY = float("inf")

class FloydWarshallRecursiveTests(unittest.TestCase):
    def test_recursive_floyd(self):
        # Define a graph as a test case
        graph1 = [[0, 5, INFINITY, 10],
                  [INFINITY, 0, 3, INFINITY],
                  [INFINITY, INFINITY, 0, 1],
                  [INFINITY, INFINITY, INFINITY, 0]]
        # Define expected result after applying the algorithm
        expected_result1 = [[0, 7, 12, 8],
                            [INFINITY, 0, 5, 7],
                            [INFINITY, INFINITY, 0, 2],
                            [INFINITY, INFINITY, INFINITY, 0]]
        # Verify that the algorithm produces the expected result
        self.assertEqual(recursive_floyd(graph1), expected_result1)

# Run the tests if the module is executed as the main program
if __name__ == '__main__':
    unittest.main()
