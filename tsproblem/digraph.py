#!/usr/bin/python
#  -*- coding: utf-8 -*-

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

    def minimum_spanning_tree(self):
        """
        Implementacion de Prim. Solo funciona para digrafos completos
        y simetricos (equivalentes a grafos no dirigidos).
        :return: arbol de tendido minimo
        """
        # Setup
        visited_nodes = []
        available_edges = []
        tree_edges = []
        node = 0

        # Execution
        while node is not None:
            visited_nodes.append(node)
            available_edges += self.vertices[node]
            available_edges.sort(key=lambda e: e.weight)
            while available_edges:
                nxt = available_edges.pop(0)
                if not nxt.dst in visited_nodes:
                    tree_edges.append(nxt)
                    node = nxt.dst
                    break
            if not available_edges:
                node = None

        # Return
        tree = Digraph(self.V())
        for edge in tree_edges:
            tree.add_edge(edge.src, edge.dst, edge.weight)
        return tree

    def get_weight(self, src, dst):
        """Devuelve el peso de la arista entre src y dst si existe"""
        edges = self.vertices[src]
        for edge in edges:
            if edge.dst == dst:
                return edge.weight
        raise ValueError("Arista no existe")
