class Edge(object):

    def __init__(self, end_vertex: int, edge_weight: int):
        self.end_vertex = end_vertex
        self.edge_weight = edge_weight

    def __hash__(self):
        return hash((self.end_vertex, self.edge_weight))

    def __eq__(self, other):
        return self.end_vertex == other.end_vertex and self.edge_weight == other.edge_weight
