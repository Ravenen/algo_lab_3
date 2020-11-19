import unittest

from graph.edge import Edge
from graph.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.first_graph = Graph()
        self.first_graph.add_bidirectional_edge_from_vertexes(1, 2, 5)
        self.first_graph.add_bidirectional_edge_from_vertexes(2, 3, 5)
        self.first_graph.add_bidirectional_edge_from_vertexes(1, 3, 15)

        self.second_graph = Graph()
        self.second_graph.add_bidirectional_edge_from_vertexes(1, 2, 50)
        self.second_graph.add_bidirectional_edge_from_vertexes(1, 3, 70)
        self.second_graph.add_bidirectional_edge_from_vertexes(3, 2, 80)
        self.second_graph.add_bidirectional_edge_from_vertexes(3, 4, 50)
        self.second_graph.add_bidirectional_edge_from_vertexes(5, 3, 60)

    def test_vertexes_quantity_first(self):
        self.assertEqual(3, len(self.first_graph.get_vertexes()))

    def test_vertexes_composition_first(self):
        self.assertSetEqual({1, 2, 3}, set(self.first_graph.get_vertexes()))

    def test_edges_quantity_first(self):
        self.assertEqual(2, len(self.first_graph.adjacencies[1]))
        self.assertEqual(2, len(self.first_graph.adjacencies[2]))
        self.assertEqual(2, len(self.first_graph.adjacencies[3]))

    def test_edges_composition_first(self):
        self.assertSetEqual({Edge(2, 5), Edge(3, 15)},
                            set(self.first_graph.adjacencies[1]))
        self.assertSetEqual({Edge(3, 5), Edge(1, 5)},
                            set(self.first_graph.adjacencies[2]))
        self.assertSetEqual({Edge(2, 5), Edge(1, 15)},
                            set(self.first_graph.adjacencies[3]))

    def test_vertexes_quantity_second(self):
        self.assertEqual(5, len(self.second_graph.get_vertexes()))

    def test_vertexes_composition_second(self):
        self.assertSetEqual({1, 2, 3, 4, 5}, set(self.second_graph.get_vertexes()))

    def test_edges_quantity_second(self):
        self.assertEqual(2, len(self.second_graph.adjacencies[1]))
        self.assertEqual(2, len(self.second_graph.adjacencies[2]))
        self.assertEqual(4, len(self.second_graph.adjacencies[3]))
        self.assertEqual(1, len(self.second_graph.adjacencies[4]))
        self.assertEqual(1, len(self.second_graph.adjacencies[5]))

    def test_edges_composition_second(self):
        self.assertSetEqual({Edge(2, 50), Edge(3, 70)},
                            set(self.second_graph.adjacencies[1]))
        self.assertSetEqual({Edge(1, 50), Edge(3, 80)},
                            set(self.second_graph.adjacencies[2]))
        self.assertSetEqual({Edge(1, 70), Edge(2, 80), Edge(4, 50), Edge(5, 60)},
                            set(self.second_graph.adjacencies[3]))
        self.assertSetEqual({Edge(3, 50)}, set(self.second_graph.adjacencies[4]))
        self.assertSetEqual({Edge(3, 60)}, set(self.second_graph.adjacencies[5]))
