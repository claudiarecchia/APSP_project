from FibHeap import *
import sys
import typing


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self):
        self.vertici = []
        self.num_vertici = 0
        self.archi = []

    def __iter__(self):
        return iter(self.vertici.values())

    def add_arco(self, nodo_partenza, nodo_arrivo, peso=0):
        # Adding the node to the source node
        node = AdjNode(nodo_arrivo.name)
        node.next = [self.archi[nodo_partenza.name], peso]
        self.archi[nodo_partenza.name] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(nodo_partenza.name)
        node.next = [self.archi[nodo_arrivo.name], peso]
        self.archi[nodo_arrivo.name] = node

        # print("add arco:", nodo_partenza.left, nodo_partenza.right, nodo_arrivo.left, nodo_arrivo.right)

    def add_nodes(self, list):
        for v in list:
            self.num_vertici = self.num_vertici + 1
            self.vertici.append(v)
            # print("v:",  v.left, v.right)
        self.archi = [None] * self.num_vertici

    def get_archi(self, u):
        adiacenza = []
        temp = self.archi[u.name]
        while not isinstance(temp, type(None)):
            copy = temp
            if isinstance(copy, typing.List):
                adiacenza.append(copy[1])
            if isinstance(temp, typing.List): temp = temp[0]
            adiacenza.append(temp.vertex)
            temp = temp.next

            if isinstance(temp[0], type(None)):
                adiacenza.append(temp[1])
                break
        # print(adiacenza)
        return adiacenza

    def get_nodo(self, n):
        return self.vertici[n]


def dijkstra(grafo, nodo_partenza):
    # Imposto la distanza di tutti i nodi a infinito (tranne la source)
    for v in grafo.vertici:
        v.key = sys.maxsize

    # definizione T (lista)
    cammino = []

    fheap = Fheap()
    # Imposto la distanza del nodo di partenza a zero
    nodo_partenza.key = 0
    fheap.insert(nodo_partenza)

    while fheap:
        print("--------------------\n")
        # Rimuovo un vertice con la distanza minore
        u = fheap.extract_min()

        if u is None:
            break

        print("Nodo estratto:", u.name)

        lista_archi_u_v = g.get_archi(u)
        print("Lista archi: ", lista_archi_u_v)
        # print(int(len(lista_archi_u_v)/2))

        i = 0
        for arco in range(int(len(lista_archi_u_v)/2)):
            print("valore i:", i)
            dist = lista_archi_u_v[i+1]

            nodo_name = lista_archi_u_v[i]
            nodo = g.get_nodo(nodo_name)

            print("nodo: ", nodo.name, " -> ", u.key, nodo.key, dist)

            if nodo.key == sys.maxsize:
                print("aggiungo all'heap")
                nodo.key = u.key + dist
                fheap.insert(nodo)

            elif u.key + dist < nodo.key:
                print("aggiorno valore nodo key con:", u.key + dist )
                # fheap.decrease_key(nodo, nodo.key - (u.key + dist))
                fheap.decrease_key(nodo, u.key + dist)
            i = i+2


def shortest(grafo, nodo_partenza):
    for vertice in grafo.vertici:
        print("Il vertice", vertice.name, "è a distanza", vertice.key, "dal nodo sorgente", nodo_partenza.name)


if __name__ == '__main__':
    g = Graph()

    a = Node(0)
    b = Node(1)
    c = Node(2)
    d = Node(3)
    e = Node(4)
    f = Node(5)

    list = [a, b, c, d, e, f]
    g.add_nodes(list)

    g.add_arco(a, b, 7)
    g.add_arco(a, c, 9)
    g.add_arco(a, f, 14)
    g.add_arco(b, d, 10)
    g.add_arco(c, d, 15)
    g.add_arco(f, e, 11)
    g.add_arco(c, e, 2)

    g.add_arco(e, d, 2)


    dijkstra(g, g.get_nodo(2))

    shortest(g, g.get_nodo(2))

    # graph = {'A': set(['B', 'C']),
    #          'B': set(['A', 'D', 'E']),
    #          'C': set(['A', 'F']),
    #          'D': set(['B']),
    #          'E': set(['B', 'F']),
    #          'F': set(['C', 'E'])}