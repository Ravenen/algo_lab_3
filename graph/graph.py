from typing import Tuple, List, Dict


class Graph(object):

    def __init__(self):
        self.adjacencies: Dict[int, List[Tuple[int, int]]] = {}

    def add_edges_from_vertexes(self, vertex_first_index: int, vertex_second_index: int, weight: int):
        self.__add_edge(vertex_first_index, vertex_second_index, weight)
        self.__add_edge(vertex_second_index, vertex_first_index, weight)
        
    def get_vertexes(self) -> List[int]:
        return list(self.adjacencies.keys())

    def __add_edge(self, vertex_from_index: int, vertex_to_index: int, weight: int):
        if vertex_from_index in self.adjacencies.keys():
            if (weight, vertex_to_index) not in self.adjacencies[vertex_from_index]:
                self.adjacencies[vertex_from_index].append((weight, vertex_to_index))
        else:
            self.adjacencies[vertex_from_index] = []
            self.adjacencies[vertex_from_index].append((weight, vertex_to_index))
