# unit test for 
# Floyd Warshall Algorithm using imperative with Python

import unittest
from floyd_algorithms import imperative_floyd
INFINITY = float("inf")

class TestFloydWarshallImperative(unittest.TestCase):
    def test_imperative_floyd(self):
        # Define the graph to be tested
        graph1 = [[0, 7, INFINITY, 8],
                  [INFINITY, 0, 5, INFINITY],
                  [INFINITY, 10, 0, 2],
                  [16, INFINITY, 4, 0]]

        # Expected results after applying the Floyd-Warshall algorithm
        expected_result1 = [[0, 7, 12, 8],
                            [INFINITY, 0, 5, 7],
                            [INFINITY, INFINITY, 0, 2],
                            [INFINITY, INFINITY, INFINITY, 0]]

        # Assert that the output from the algorithm matches the expected result
        self.assertEqual(imperative_floyd(graph1), expected_result1)

# Execute the tests if the script is run directly
if __name__ == '__main__':
    unittest.main()
