from digraph import Digraph


def aprox_tsp_algorithm(graph):
    """
    Assumes: graph is complete and symmetric or not directed,
    and satisfies the triangular inequality
    :param graph: source graph
    :return: approximate solution to the traveling salesman problem
    """
    minimum_spanning_tree = graph.minimum_spanning_tree()

    vertices = [0]
    tree_traversal(minimum_spanning_tree, 0, vertices)

    solution = Digraph(graph.V())
    for i in range(len(vertices)):
        if i == len(vertices) - 1:
            solution.add_edge(vertices[i], vertices[0], graph.get_weight(vertices[i], vertices[0]))
        else:
            solution.add_edge(vertices[i], vertices[i+1], graph.get_weight(vertices[i], vertices[i+1]))

    return solution


def tree_traversal(graph, node, visited_vertices):
    for vertex in graph.adj(node):
        visited_vertices.append(vertex)
        tree_traversal(graph, vertex, visited_vertices)


def graph_from_file(filename):
    f = open(filename, 'r')
    model_matrix = []
    for line in f:
        model_matrix.append([int(s) for s in line.split(' ')])
    f.close()

    graph = Digraph(len(model_matrix))
    for i in range(len(model_matrix)):
        for j in range(len(model_matrix[i])):
            graph.add_edge(i, j, model_matrix[i][j])

    return graph


def aprox_tsp(filename):
    return aprox_tsp_algorithm(graph_from_file(filename))
