from math import sqrt
from aprox_tsp import *
import timeit


def h(a, b):
    return sqrt(a**2 + b**2)

if __name__ == "__main__":
    # Del ejemplo de Cormen, 35.2.1, imagen 35.2:
    #   a, b, c, d, e, f, g, h
    #   0, 1, 2, 3, 4, 5, 6, 7
    m = [
        [0, 2, h(1, 3), 2, h(1, 3), h(2, 2), h(2, 4), h(1, 4)],
        [2, 0, h(1, 1), h(2, 2), h(1, 3), 2, 4, h(1, 2)],
        [h(1, 3), h(1, 1), 0, h(3, 3), h(2, 4), h(1,3), h(1,5), h(1,2)],
        [2, h(2,2), h(3,3), 0, h(1,1), 2, h(2,2), h(1,4)],
        [h(1,3), h(1,3), h(2,4), h(1,1), 0, h(1,1), h(1,1), h(2,3)],
        [h(2,2), 2, h(1,3), 2, h(1,1), 0, 2, h(1,2)],
        [h(2,4), 4, h(1,5), h(2,2), h(1,1), 2, 0, h(2,3)],
        [h(1,4), h(1,2), h(1,2), h(1,4), h(2,3), h(1,2), h(2,3), 0]
    ]
    ROOT = 0
    g = graph_from_adj_matrix(m)
    mst = g.minimum_spanning_tree(ROOT)
    sol = aprox_tsp_algorithm(g, ROOT)

    # Verificamos el MST:
    exp_e = [ #(src, dst)
        (0,1), (1,2), (1,7), (0,3), (3,4), (4,5), (4,6)
    ]
    mst_ok = mst.E() == len(exp_e)  # 7 == V - 1
    for e in mst.iter_edges():
        mst_ok = mst_ok and (e.src, e.dst) in exp_e

    print "El arbol de tendido minimo es el correcto:", str(mst_ok)

    # Verificamos el ciclo del tsp:
    exp_path = [0, 1, 2, 7, 3, 4, 5, 6, 0]  # a, b, c, h, d, e, f, g, a
    print "El ciclo aproximado es el correcto:", exp_path == sol

    # Verificamos el costo del ciclo:
    # el costo deberia ser de 19.074, imponemos limites:
    exp_cost_lower = 19.07
    exp_cost_higher = 19.08

    costo = 0
    for i in xrange(len(sol) - 1):
        costo += m[sol[i]][sol[i + 1]]

    costo_ok = exp_cost_lower < costo < exp_cost_higher
    print "El costo del ciclo aprox. es el correcto", costo_ok

    # Tiempo de ejecucion
    print "\nTiempo de ejecucion"
    start_time = timeit.default_timer()
    m = matrix_from_file("matrices/p01.m")
    g = graph_from_adj_matrix(m)
    mst = g.minimum_spanning_tree(ROOT)
    p01 = aprox_tsp_algorithm(g, ROOT)
    res = timeit.default_timer() - start_time
    print "15 nodos:", res, "segundos"
    start_time = timeit.default_timer()
    m = matrix_from_file("matrices/gr17.m")
    g = graph_from_adj_matrix(m)
    mst = g.minimum_spanning_tree(ROOT)
    gr17 = aprox_tsp_algorithm(g, ROOT)
    res = timeit.default_timer() - start_time
    print "17 nodos:", res, "segundos"
    start_time = timeit.default_timer()
    m = matrix_from_file("matrices/fri26.m")
    g = graph_from_adj_matrix(m)
    mst = g.minimum_spanning_tree(ROOT)
    fri26 = aprox_tsp_algorithm(g, ROOT)
    res = timeit.default_timer() - start_time
    print "26 nodos", res, "segundos"
