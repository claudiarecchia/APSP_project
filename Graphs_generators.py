from datetime import time

import networkit as nk
import random
from Global_variables import *
from IO_utilities import *


def create_barabasi_albert_graph(n_vertici, file_name):
    bara_graph = nk.generators.BarabasiAlbertGenerator(k, n_vertici, n0=0, batagelj=True).generate()
    # print("numero nodi", bara_graph.numberOfNodes(), "- numero archi", bara_graph.numberOfEdges())

    connections = []
    for u, v in bara_graph.iterEdges():
        if u != v:  # no self-loop
            connections.append([u, v, randint(0, MAX)])

    # print("------------------------------------------")
    # for element in connections:
    #     print(element)

    write_connections_to_file(connections, file_name)
    connections, vertices_list = create_connections_from_file_real_graph(file_name)
    return connections, vertices_list


# Utilizzo la Linear Congruential (LC) per generare dei valori randomici uniformi
# (generatore pseudo-random perchè il risultato i+1-esimo dipende dall'i-esimo)
# rng.current è il seed [ s = ( a*s+b ) % m ]
# quindi il seed viene aggiornato ad ogni esecuzione della funzione
# i valori a,b,m vengono scelti opportunamente in base a principi della teoria dei numeri
# il metodo base genera interi ma lo uso per generare valori apparteneti all'intervallo [0,1)
# dividendo il risultato per m stesso (nella funzione create_ER_graph)
def rng(M=m, A=a, B=b):
    rng.current = (A * rng.current + B) % M
    return rng.current


def create_ER_graph(vertici, m, file_name):
    """ Creazione di un grafo in maniera randomica secondo il modello ER """
    # tempo di sistema per l'inizializzazione del seed: difficile da replicare
    rng.current = int(round(time.time() * 1000))
    connections = []
    for i in vertici:
        for j in vertici:
            # invocazione della funzione rng con m come modulo, mentre a,b sono impostati nel file Global_variables.py
            if round(rng(m) / m < p):
                if i != j:  # no self-loop
                    peso = randint(1, MAX)
                    connections.append((i, j, peso))
    write_connections_to_file(connections, file_name)
    return connections


def create_path_graph(vertici, file_name):
    """
    Creazione di un grafo a path (in cui il nodo i-esimo è connesso solamente al nodo i+1-esimo)
    con m nodi e la cui struttura viene salvata sul file il cui nome è passato per parametro
    """
    connections = []
    for i in range(len(vertici) - 1):
        peso = randint(1, MAX)
        connections.append((vertici[i], vertici[i+1], peso))
    write_connections_to_file(connections, file_name)
    return connections
