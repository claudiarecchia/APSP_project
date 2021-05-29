"""
Implementazione dell'algoritmo SSSP di Dijkstra
Utilizzando una rappresentazione del grafo attraverso le liste di adiacenza
Considerando per ogni arco anche il proprio peso (non negativo)
E sfruttando il Fibonacci Heap come coda con priorità
Algoritmo per grafi orientati o non orientati e con un vertice sorgente S
"""

from IO_utilities import *
from Graph import *


def dijkstra(grafo, nodo_partenza):
    """ Implementazione dell'algoritmo SSSP Dijkstra """
    for v in grafo.vertici:
        v.key = sys.maxsize

    fheap = makefheap()
    nodo_partenza.key = 0
    nodo_partenza.added = True
    fheap.insert(nodo_partenza)

    while fheap.num_nodes > 0:
        u = fheap.extract_min()
        lista_archi_u_v = grafo.get_edges(u)
        for i in range(len(lista_archi_u_v)):

            # # controllo per matrice di adiacenza se v=u
            # if isinstance(lista_archi_u_v[0], int):
            #     if u.name != i:
            #         dist = lista_archi_u_v[i]
            #         v = grafo.vertici[i]
            #     else:
            #         # se u=v allora procedo con il prossimo elemento nella lista di adiacenza
            #         continue
            # else:

            arco = lista_archi_u_v[i]
            v = arco[0]
            dist = arco[1]

            if v.key == sys.maxsize and not v.added:
                v.key = u.key + dist
                v.added = True
                fheap.insert(v)

            elif u.key + dist < v.key:
                fheap.decrease_key(v, u.key + dist)


def shortest(grafo, nodo_partenza, mat):
    for vertice in grafo.vertici:
        # print("Il vertice", vertice.name, "è a distanza", vertice.key, "dal nodo sorgente", nodo_partenza.name)
        mat[int(nodo_partenza.name)][int(vertice.name)] = vertice.key




