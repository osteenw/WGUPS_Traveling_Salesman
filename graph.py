# Will Osteen
# Student ID 001099825
# From section 6.12 of the DSA 2 zyBook on Dijkstra's algorithm in Python.

# Graph and Vertex Classes
class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None
