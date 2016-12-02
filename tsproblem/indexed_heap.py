#!/usr/bin/python
#  -*- coding: utf-8 -*-
from heapq import heapify


class IndexedHeap(object):
    """Implementa un heap (de minimo) con indizacion de elementos
    para poder modificarlos en su lugar, sosteniendo la invariante.
    Idealmente utilizar como un contenedor normal.
    Opcionalmente utilizar los metodos "privados".
    """

    def __init__(self, data_inicial=list()):
        """
        :param data_inicial: (Opcional) Una lista con tuplas (prioridad, clave)
        """
        super(IndexedHeap, self).__init__()
        self.heap = list(data_inicial)
        heapify(self.heap)
        self.index = {self.heap[i][1]: i for i in xrange(len(self.heap))}

    def __nonzero__(self):
        return bool(self.heap)

    def __contains__(self, item):
        return item in self.index

    def pop(self):
        last = self.heap.pop()  # raises appropriate IndexError if heap is empty
        if self.heap:
            return_item = self.heap[0]
            self.heap[0] = last
            self.index[last[1]] = 0
            self._downheap(0)
        else:
            return_item = last
        del self.index[return_item[1]]
        return return_item[1]

    def __getitem__(self, key):
        return self.heap[self.index[key]][0]

    def __setitem__(self, key, priority):
        if key in self.index:
            # Modificamos la prioridad:
            i = self.index[key]
            old_priority = self.heap[i][0]
            self.heap[i] = (priority, key)
            if priority < old_priority: # disminuyo!
                self._upheap(0, i)
            elif priority > old_priority: # aumento!
                self._downheap(i)
            # else: pass
        else:
            self._push(key, priority)

    # OJO: Usar aparte solo si se sabe lo que hace:
    def _push(self, key, priority):
        self.heap.append((priority, key))
        self._upheap(0, len(self.heap) - 1)

    # OJO: Usar aparte solo si se sabe lo que hace:
    def _decreaseKey(self, key, new_priority):
        # DOY POR SENTADO QUE ME PASAN PRIORIDAD MENOR!:
        i = self.index[key]
        self.heap[i] = (new_priority, key)
        self._upheap(0, i)

    def _upheap(self, startpos, i):
        """Credits to heapq: con un par de cambios"""
        son = self.heap[i]
        parent_i = (i - 1) >> 1 # == (i-1) / 2**1
        parent = self.heap[parent_i]
        while i > startpos and son[0] < parent[0]:
            #Seteo solo el padre, quizas me sigo moviendo
            self.heap[i] = parent
            self.index[parent[1]] = i
            i = parent_i
            parent_i = (i - 1) >> 1 # == (i-1) / 2**1
            parent = self.heap[parent_i]
        #Lo seteo recien cuando soy mayor que el padre
        self.heap[i] = son
        self.index[son[1]] = i

    def _downheap(self, pos):
        """Credits to heapq: practicamente igual"""
        endpos = len(self.heap)
        parent = self.heap[pos]
        left_child_pos = 2 * pos + 1  # leftmost child position
        while left_child_pos < endpos:
            # left_child_pos queda como posicion del menor
            right_child_pos = left_child_pos + 1
            if right_child_pos < endpos and self.heap[left_child_pos][0] >= self.heap[right_child_pos][0]:
                left_child_pos = right_child_pos

            # Seteamos child en parent si corresponde:
            child = self.heap[left_child_pos]
            if child[0] < parent[0]:
                self.heap[pos] = child
                self.index[child[1]] = pos
                pos = left_child_pos
                left_child_pos = 2 * pos + 1
                continue
            break
        # Lo seteo recien cuando soy <= al hijo
        self.heap[pos] = parent
        self.index[parent[1]] = pos