import unittest
from graph.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.first_graph = Graph()
        self.first_graph.add_edges_from_vertexes(1, 2, 5)
        self.first_graph.add_edges_from_vertexes(2, 3, 5)
        self.first_graph.add_edges_from_vertexes(1, 3, 15)

        self.second_graph = Graph()
        self.second_graph.add_edges_from_vertexes(1, 2, 50)
        self.second_graph.add_edges_from_vertexes(1, 3, 70)
        self.second_graph.add_edges_from_vertexes(3, 2, 80)
        self.second_graph.add_edges_from_vertexes(3, 4, 50)
        self.second_graph.add_edges_from_vertexes(5, 3, 60)

    def test_vertexes_quantity_first(self):
        self.assertEqual(len(self.first_graph.get_vertexes()), 3)

    def test_vertexes_composition_first(self):
        self.assertSetEqual(set(self.first_graph.get_vertexes()), {1, 2, 3})

    def test_edges_quantity_first(self):
        self.assertEqual(len(self.first_graph.adjacencies[1]), 2)
        self.assertEqual(len(self.first_graph.adjacencies[2]), 2)
        self.assertEqual(len(self.first_graph.adjacencies[3]), 2)

    def test_edges_composition_first(self):
        self.assertSetEqual(set(self.first_graph.adjacencies[1]), {(5, 2), (15, 3)})
        self.assertSetEqual(set(self.first_graph.adjacencies[2]), {(5, 3), (5, 1)})
        self.assertSetEqual(set(self.first_graph.adjacencies[3]), {(5, 2), (15, 1)})

    def test_vertexes_quantity_second(self):
        self.assertEqual(len(self.second_graph.get_vertexes()), 5)

    def test_vertexes_composition_second(self):
        self.assertSetEqual(set(self.second_graph.get_vertexes()), {1, 2, 3, 4, 5})

    def test_edges_quantity_second(self):
        self.assertEqual(len(self.second_graph.adjacencies[1]), 2)
        self.assertEqual(len(self.second_graph.adjacencies[2]), 2)
        self.assertEqual(len(self.second_graph.adjacencies[3]), 4)
        self.assertEqual(len(self.second_graph.adjacencies[4]), 1)
        self.assertEqual(len(self.second_graph.adjacencies[5]), 1)

    def test_edges_composition_second(self):
        self.assertSetEqual(set(self.second_graph.adjacencies[1]), {(50, 2), (70, 3)})
        self.assertSetEqual(set(self.second_graph.adjacencies[2]), {(50, 1), (80, 3)})
        self.assertSetEqual(set(self.second_graph.adjacencies[3]), {(70, 1), (80, 2), (50, 4), (60, 5)})
        self.assertSetEqual(set(self.second_graph.adjacencies[4]), {(50, 3)})
        self.assertSetEqual(set(self.second_graph.adjacencies[5]), {(60, 3)})
