import unittest
import copy

from graph.graph import Graph
from graph.search_algorithm import search_shortest_paths_from


class TestSearchAlgorithm(unittest.TestCase):

    def setUp(self) -> None:
        self.first_graph = Graph()
        self.first_graph.add_bidirectional_edge_from_vertexes(1, 2, 10)
        self.first_graph.add_bidirectional_edge_from_vertexes(1, 5, 70)
        self.first_graph.add_bidirectional_edge_from_vertexes(2, 3, 20)
        self.first_graph.add_bidirectional_edge_from_vertexes(3, 4, 20)
        self.first_graph.add_bidirectional_edge_from_vertexes(4, 5, 10)
        self.first_graph.add_bidirectional_edge_from_vertexes(5, 6, 10)

    def test_search_shortest_paths_from_first(self):
        shortest_paths = search_shortest_paths_from(1, self.first_graph)
        self.assertEqual(60, shortest_paths[5])

    def test_search_shortest_paths_from_second(self):
        shortest_paths = search_shortest_paths_from(1, self.first_graph)
        self.assertEqual(70, shortest_paths[6])

    def test_search_shortest_paths_from_third(self):
        second_graph = copy.deepcopy(self.first_graph)
        second_graph.add_bidirectional_edge_from_vertexes(1, 6, 40)
        shortest_paths = search_shortest_paths_from(1, second_graph)
        self.assertEqual(50, shortest_paths[5])
