"""
Implementazione dell'algoritmo SSSP di Dijkstra
(Esecuzione ripetuta per n volte, dove n è il numero di vertici del grafo
per ottenere un algoritmo APSP)
Utilizzando una rappresentazione del grafo attraverso le liste di adiacenza
Considerando per ogni arco anche il proprio peso (non negativo)
E sfruttando il Fibonacci Heap come coda con priorità
Algoritmo per grafi orientati o non orientati e con un vertice sorgente S
"""

from FibHeap import *
from timeit import default_timer as timer
import sys
from IO_utilities import *
from Grafo import *


def dijkstra(grafo, nodo_partenza):
    """ Implementazione dell'algoritmo SSSP Dijkstra """
    # cpu = timer()
    # Imposto la distanza di tutti i nodi a infinito
    for v in grafo.vertici:
        v.key = sys.maxsize

    fheap = makefheap()
    # Imposto la distanza del nodo di partenza a zero
    nodo_partenza.key = 0
    nodo_partenza.added = True
    fheap.insert(nodo_partenza)

    while fheap.num_nodes > 0:
        # print("--------------------\n")
        # Rimuovo un vertice con la distanza minore
        u = fheap.extract_min()
        # print("Nodo estratto:", u.name)

        lista_archi_u_v = grafo.get_archi(u)
        # print("Lista di adiacenza: ", lista_archi_u_v)

        for i in range(len(lista_archi_u_v)):
            # controllo per matrice di adiacenza se v=u
            if isinstance(lista_archi_u_v[0], int):
                if u.name != i:
                    dist = lista_archi_u_v[i]
                    v = grafo.vertici[i]
                else:
                    continue
            else:
                arco = lista_archi_u_v[i]
                v = arco[0]
                dist = arco[1]

            # print("nodo: ", v.name, " -> ", u.key, v.key, dist)

            if v.key == sys.maxsize and not v.added:
                v.key = u.key + dist
                # print("aggiungo all'heap con key", v.key)
                v.added = True
                fheap.insert(v)

            elif u.key + dist < v.key:
                # print("aggiorno valore nodo key con:", u.key + dist)
                fheap.decrease_key(v, u.key + dist)

        # time = round(timer() - cpu, 6)
        # print("TEMPO CPU:", time, "\n/////////////////////////////////////////////////////////////////////////////\n\n")


def shortest(grafo, nodo_partenza):
    for vertice in grafo.vertici:
        print("Il vertice", vertice.name, "è a distanza", vertice.key, "dal nodo sorgente", nodo_partenza.name)




