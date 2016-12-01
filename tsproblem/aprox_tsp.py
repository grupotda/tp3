from digraph import Digraph
import sys


def matrix_from_file(filename):
    """ Devuelve la matriz generada desde el archivo """
    model_matrix = []
    with open(filename, 'r') as f:
        for line in f:
            model_matrix.append([int(s) for s in line.split(' ')])
    return model_matrix


def graph_from_adj_matrix(matrix):
    """ Devuelve el Digrafo generado a partir de la matriz de ady. """
    graph = Digraph(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            graph.add_edge(i, j, matrix[i][j])
    return graph


def preorder_tree_traversal(tree, root):
    """ Devuelve lista de vertices con el recorrido en preorder """
    vertices = []
    _preorder_tree_traversal(tree, root, vertices)
    return vertices


def _preorder_tree_traversal(tree, v, vertices):
    """ Funcion recursiva para el recorrido en preorder"""
    vertices.append(v)
    for w in tree.adj(v):
        _preorder_tree_traversal(tree, w, vertices)


def aprox_tsp_algorithm(graph, start_vertex=0):
    """
    Asumimos: el grafo es completo, simetrico y no dirigido.
    Tambien debe satisfacer la desigualdad triangular.
    :param graph: Digraph comportandose como grafo
    :return: lista de vertices que forman un ciclo que es
        una solucion aproximada del problema del viajante
    """
    mst = graph.minimum_spanning_tree(start_vertex)
    vertices = preorder_tree_traversal(mst, start_vertex)
    vertices.append(vertices[0])
    return vertices


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print "Uso: aprox_tsp.py <file>"
    else:
        START_VERTEX = 0
        adj_matrix = matrix_from_file(sys.argv[1])
        graph = graph_from_adj_matrix(adj_matrix)
        sol = aprox_tsp_algorithm(graph, START_VERTEX)
        costo = 0
        for i in xrange(len(sol)-1):
            costo += adj_matrix[sol[i]][sol[i+1]]

        print "Recorrido: "
        print sol
        print "Costo = %d" % costo
