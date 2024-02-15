def oracle(graph) --> bool:
    pass

class G():
    def __init__(self, vertices, edges):
        self.V = vertices
        self.n = len(self.V)
        self.E = edges
        self.m = len(self.E)
    def get_vertex_at_index(self, index):
        return self.V[index]
    def get_adjacent_vertecies(self, index):
        adjacent_vertecies = []
        return adjacent_vertecies

class Vertex():
    def __init__(self):
        self.color = None

def init_vertices():
    pass
def init_edges(vertices):
    pass

def pick_available_color(vertex, graph):
    pass
def no_conflicts(vertex, graph):
    pass
def init_a_graph():
    vertices = init_vertices()
    edges = init_edges(vertices)
    graph = G(vertices, edges)
    return graph

def remove_vertex_and_adjacent_edges(vertex, graph):

    pass
    return graph
def algorithm_in_poly_time(graph):
    n = graph.n

    if n <= 1:
        return True

    vertex_i = graph.get_vertex_at_index(i)
    vertex_i_can_be_colorized = no_conflicts(vertex_i, graph)
    if not vertex_i_can_be_colorized:
        return False
    else:
        pick_available_color(vertex_i, graph)

    graph_can_be_colorized = oracle(graph)
    if graph_can_be_colorized:
        return True
    else:
        graph = remove_vertex_and_adjacent_edges(vertex_i, graph)
        algorithm_in_poly_time(graph)




if __name__ == "__main__":

    graph = init_a_graph()






