from heapq import heappush, heappop
from typing import Dict

from graph.graph import Graph


def search_shortest_paths_from(start_index: int, graph: Graph) -> Dict[int, int]:
    return dijkstra_algorithm(start_index, graph)


def dijkstra_algorithm(base_index: int, graph: Graph) -> Dict[int, int]:
    queue = []
    heappush(queue, (0, base_index))
    weights = {base_index: 0}

    while queue:
        current_weight, current_vertex_index = heappop(queue)
        neighbour_vertexes = graph.adjacencies[current_vertex_index]
        for neighbour_vertex in neighbour_vertexes:
            weight, vertex_index = neighbour_vertex
            total_weight = current_weight + weight
            if vertex_index not in weights.keys() or total_weight < weights[vertex_index]:
                weights[vertex_index] = total_weight
                heappush(queue, (total_weight, vertex_index))

    return weights
