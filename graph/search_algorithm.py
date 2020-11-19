from heapq import heappush, heappop
from typing import Dict, List, Tuple

from graph.edge import Edge
from graph.graph import Graph


def search_shortest_paths_from(start_index: int, graph: Graph) -> Dict[int, int]:
    return dijkstra_algorithm(start_index, graph.adjacencies)


def dijkstra_algorithm(base_index: int, adjacency_list: Dict[int, List[Edge]]) -> Dict[int, int]:
    queue = []
    heappush(queue, (0, base_index))
    weights = {base_index: 0}

    while queue:
        current_weight, current_vertex = heappop(queue)
        current_vertex_edges = adjacency_list[current_vertex]

        for edge in current_vertex_edges:
            edge_weight = edge.edge_weight
            neighbour_vertex = edge.end_vertex

            total_path_weight = current_weight + edge_weight
            if neighbour_vertex not in weights.keys() or total_path_weight < weights[neighbour_vertex]:
                weights[neighbour_vertex] = total_path_weight
                heappush(queue, (total_path_weight, neighbour_vertex))

    return weights
