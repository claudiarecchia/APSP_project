"""
Implementazione dell'algoritmo SSSP di Dijkstra
(Esecuzione ripetuta per n volte, dove n è il numero di vertici del grafo
per ottenere un algoritmo APSP)
Utilizzando una rappresentazione del grafo attraverso le liste di adiacenza
Considerando per ogni arco anche il proprio peso
E sfruttando il Fibonacci Heap come coda con priorità per la gestione dei vertici
"""

from FibHeap import *
from timeit import default_timer as timer
import sys
from random import *
import time


class Graph(object):
    """ Struttura del grafo  """
    def __init__(self, vertici, directed=False):
        self.vertici = vertici
        self._graph = {}
        self.init()
        self._directed = directed

    def init(self):
        """ Inizializzazione del grafo """
        for i in range(len(self.vertici)):
            self._graph[i] = []

    def make_connections(self):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, nodo1, nodo2):
        """ Aggiunge un arco (senza peso) tra i nodo1 e nodo2 """

        nodo_peso_dir = [nodo2, None]
        if nodo_peso_dir not in self._graph[nodo1.name]:
            self._graph[nodo1.name].append(nodo_peso_dir)
        if not self._directed:
            nodo_peso_ndir = [nodo1, None]
            if nodo_peso_ndir not in self._graph[nodo2.name]:
                self._graph[nodo2.name].append(nodo_peso_ndir)

    def add_weights(self):
        """
        Aggiunge un peso ad ogni arco
        Se il grafo è non orientato, aggiunge il peso dell'arco u,v
        anche all'arco v,u
        """

        for vertice in range(0, n):
            adj_list = self._graph[vertice]
            for i in range(0, len(adj_list)):
                if adj_list[i][1] is None:
                    peso = randint(1, 50)
                    adj_list[i][1] = peso
                    if not self._directed:
                        adj_list_vertex_2 = self._graph[int(adj_list[i][0].name)]
                        for j in range(0, len(adj_list_vertex_2)):
                            if adj_list_vertex_2[j][0].name == vertice:
                                if adj_list_vertex_2[j][1] is None:
                                    adj_list_vertex_2[j][1] = peso

    def print_grafo(self):
        """
        Stampa del grafo
        Per ogni vertice è presente la lista di adiacenza nella forma (nodo, peso)
        """

        for vertice in self._graph:
            adj_list = self._graph[vertice]
            print("Vertice " + str(vertice) + ":", end="")
            for i in range(0, len(adj_list)):
                print(" -> ({},".format(adj_list[i][0].name), "{})".format(adj_list[i][1]), end="")
            print(" \n")

    def get_archi(self, u):
        """ Ritorna la lista di adiacenza dell nodo u """
        adiacenza = self._graph[u.name]
        return adiacenza

    def get_nodo(self, n):
        """ Ritorna l'oggetto nodo richiesto """
        return self.vertici[n]


def dijkstra(grafo, nodo_partenza):
    """ Implementazione della funzione SSSP Dijkstra """

    cpu = timer()

    # Imposto la distanza di tutti i nodi a infinito (tranne la source)
    for v in grafo.vertici:
        v.key = sys.maxsize

    fheap = Fheap()
    # Imposto la distanza del nodo di partenza a zero
    nodo_partenza.key = 0
    fheap.insert(nodo_partenza)

    while fheap:
        print("--------------------\n")
        # Rimuovo un vertice con la distanza minore
        u = fheap.extract_min()

        # Condizioe di arresto della funzione
        if u is None:
            break

        print("Nodo estratto:", u.name)

        lista_archi_u_v = g.get_archi(u)
        print("Lista di adiacenza: ", lista_archi_u_v)

        for i in range(len(lista_archi_u_v)):
            arco = lista_archi_u_v[i]

            v = arco[0]
            dist = arco[1]

            print("nodo: ", v.name, " -> ", u.key, v.key, dist)

            if v.key == sys.maxsize:
                print("aggiungo all'heap")
                v.key = u.key + dist
                fheap.insert(v)

            elif u.key + dist < v.key:
                print("aggiorno valore nodo key con:", u.key + dist)
                print("nuovo valore:", v.name, u.key + dist)
                fheap.decrease_key(v, u.key + dist)

    time = round(timer() - cpu, 6)
    print("TEMPO CPU:", time, "\n\n")


def shortest(grafo, nodo_partenza):
    for vertice in grafo.vertici:
        print("Il vertice", vertice.name, "è a distanza", vertice.key, "dal nodo sorgente", nodo_partenza.name)


m = 2 ** 32
b = 12345
a = 1103515245
def rng(M=m, A=a, B=b):
    rng.current = (A * rng.current + B) % M
    return rng.current


if __name__ == '__main__':

    connections = []

    rng.current = int(round(time.time() * 1000))
    n = 7  # n vertici

    vertici = []
    for i in range(n):
        vertici.append(Node(i))

    g = Graph(vertici, directed=False)

    p = 0.45  # probabilità

    for i in vertici:
        for j in vertici:
            if round(rng(m) / m) > p:
                if i != j:  # no self-loop
                    connections.append((i, j))

    g.make_connections()
    g.add_weights()
    g.print_grafo()


    dijkstra(g, g.get_nodo(2))
    # shortest(g, g.get_nodo(2))

