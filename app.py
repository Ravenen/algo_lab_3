from graph.graph import Graph
from graph.search_algorithm import search_shortest_paths_from

if __name__ == '__main__':

    graph = Graph()
    graph.add_edges_from_vertexes(1, 3, 10)
    graph.add_edges_from_vertexes(3, 4, 80)
    graph.add_edges_from_vertexes(4, 5, 50)
    graph.add_edges_from_vertexes(5, 6, 20)
    graph.add_edges_from_vertexes(2, 3, 40)
    graph.add_edges_from_vertexes(2, 4, 100)

    clients_indexes = [1, 2, 6]
    min_latency = -1

    for vertex_index in graph.get_vertexes():
        if vertex_index not in clients_indexes:
            shortest_paths = search_shortest_paths_from(vertex_index, graph)
            current_max_latency = max([shortest_paths[client_index] for client_index in clients_indexes])
            if min_latency == -1:
                min_latency = current_max_latency
            else:
                min_latency = current_max_latency if current_max_latency < min_latency else min_latency

    print(min_latency)
