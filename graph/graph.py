from collections import defaultdict
from typing import List, DefaultDict

from graph.edge import Edge


class Graph(object):

    def __init__(self):
        self.adjacencies: DefaultDict[int, List[Edge]] = defaultdict(list)

    def add_bidirectional_edge_from_vertexes(self, vertex_first: int, vertex_second: int, weight: int):
        self.__add_edge(vertex_first, vertex_second, weight)
        self.__add_edge(vertex_second, vertex_first, weight)
        
    def get_vertexes(self) -> List[int]:
        return list(self.adjacencies.keys())

    def __add_edge(self, vertex_from: int, vertex_to: int, weight: int):
        self.adjacencies[vertex_from].append(Edge(vertex_to, weight))

