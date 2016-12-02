#!/usr/bin/python
#  -*- coding: utf-8 -*-
from indexed_heap import IndexedHeap


class Edge:
    """
    Arista de un grafo
    """

    def __init__(self, src, dst, weight):
        """
        Construye una arista de un grafo
        :param src: vertice de origen de la arista
        :param dst: vertice al que esta destinado la arista
        :param weight: peso de la arista
        """
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return "%d->%d (%d)" % (self.src, self.dst, self.weight)


class Digraph:
    """
    Grafo no dirigido con un número fijo de vértices.

    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
    nuevas aristas.
    """

    def __init__(self, V):
        """
        Construye un grafo sin aristas de V vertices.
        :param V: cantidad de vertices
        """
        self.vertices = [[] for _ in xrange(V)]

    def V(self):
        """
        :return: Cantidad de vertices en el grafo.
        """
        return len(self.vertices)

    def E(self):
        """
        :return: Cantidad de aristas en el grafo.
        """
        return sum(len(aristas) for aristas in self.vertices)

    def adj_e(self, v):
        """
        Itera sobre los aristas salientes de v.
        :param v: vertice origen, debe pertenecer al grafo
        :return: iterador de Aristas
        """
        return iter(self.vertices[v])

    def adj(self, v):
        """
        Itera sobre los vertices adyacentes a v.
        Nota: los vertices adyacentes a v son a los que inciden sus aristas. VER!
        :param v: vertice origen, debe pertenecer al grafo
        :return: iterador de vertices
        """
        # Uso un set para no tener elementos duplicados
        return iter(set(a.dst for a in self.vertices[v]))

    def add_edge(self, src, dst, weight=1):
        """
        Añade una arista al grafo.
        :param src: el vertice origen, debe pertenecer al grafo.
        :param dst: el vertice destino, debe pertenecer al grafo.
        :param weight: el peso asociado a la arista.
        """
        if dst >= self.V(): raise IndexError("Vertice desconocido")
        self.vertices[src].append(Edge(src, dst, weight))

    def __iter__(self):
        """
        Itera sobre los vertices del grafo, de 0 a V.
        """
        return iter(range(self.V()))

    def iter_edges(self):
        """
        Itera sobre todas las aristas del grafo.
        """
        for aristas in self.vertices:
            for edge in aristas:
                yield edge

    def minimum_spanning_tree(self, root=0):
        """
        Implementacion del algoritmo de Prim.
        Da por sentado que esta instancia de Digrafo es un Grafo. Es decir, que
        una arista esta representada por dos aristas dirigidas del mismo peso.
        Inicia el algoritmo desde el vertice raiz "root", por defecto = 0.
        :return Digraph: arbol de tendido minimo dirigido
        """
        # Setup
        visited = [False] * self.V()
        # edge_to = {dstVertex: Edge(srcVertex, dstVertex, weight)}
        edge_to = {}
        # heap inicializado con vertice raiz del arbol
        heap = IndexedHeap()
        heap._push(root, 0)

        # Execution
        while heap:
            v = heap.pop()
            visited[v] = True

            for e in self.adj_e(v):
                if not visited[e.dst]:
                    new_priority = e.weight
                    if e.dst in heap:
                        if new_priority < heap[e.dst]:
                            edge_to[e.dst] = e
                            heap._decreaseKey(e.dst, new_priority)
                    else:
                        edge_to[e.dst] = e
                        heap._push(e.dst, new_priority)

        # Return
        tree = Digraph(self.V())
        for edge in edge_to.values():
            tree.add_edge(edge.src, edge.dst, edge.weight)
        return tree

    def get_weight(self, src, dst):
        """Devuelve el peso de la arista entre src y dst si existe"""
        edges = self.vertices[src]
        for edge in edges:
            if edge.dst == dst:
                return edge.weight
        raise ValueError("Arista no existe")
