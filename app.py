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

    min_latency = -1
    for vertex_index in graph.get_vertexes():
        if vertex_index not in clients_indexes:
            shortest_paths = search_shortest_paths_from(vertex_index, graph)
            current_max_latency = max([shortest_paths[client_index] for client_index in clients_indexes])
            if min_latency == -1:
                min_latency = current_max_latency
            else:
                min_latency = current_max_latency if current_max_latency < min_latency else min_latency

    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(min_latency))

    print(min_latency)
