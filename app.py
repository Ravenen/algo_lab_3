from typing import List

from graph.graph import Graph
from graph.search_algorithm import search_shortest_paths_from

INPUT_FILE_NAME = "gamsrv.in"
OUTPUT_FILE_NAME = "gamsrv.out"


def string_to_int_list(string: str) -> List[int]:
    int_list = [int(value_str) for value_str in string.strip().split()]
    return int_list


if __name__ == '__main__':

    graph = Graph()

    with open(INPUT_FILE_NAME, "r") as input_file:
        number_of_nodes, number_of_connections = string_to_int_list(input_file.readline())
        clients = string_to_int_list(input_file.readline())
        for line in input_file:
            start_node, end_node, latency = string_to_int_list(line)
            graph.add_bidirectional_edge_from_vertexes(start_node, end_node, latency)

    min_latency = 1e12
    for vertex in graph.get_vertexes():
        if vertex not in clients:
            shortest_paths = search_shortest_paths_from(vertex, graph)
            current_max_latency = max([shortest_paths[client] for client in clients])
            min_latency = min(current_max_latency, min_latency)

    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(min_latency))

    print(min_latency)
