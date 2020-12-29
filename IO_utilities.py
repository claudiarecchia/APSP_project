"""
In questo file è presente una funzione utile per la creazione di un grafo in maniera randomica,
sfruttando il modello Erdős–Rényi (basato sulle variabili globali m, b, a)
"""

import time
import csv
from random import *
from FibHeap import *
from Global_variables import *


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


def write_connections_to_file(connections, file_name):
    """
    Nel caso in cui nell'algoritmo di Dijkstra o Floyd-Warshall venga creato un nuovo grafo,
    attraverso tale funzione è possibile rendere replicabile l'esecuzione dell'esperimento
    trascrivendo su un file il grafo generato
    """
    with open('grafi_csv/' + file_name + '.csv', mode='w') as graph_file:
        fieldnames = ['nodo_partenza', 'nodo_arrivo', 'peso_arco']
        writer = csv.DictWriter(graph_file, fieldnames=fieldnames)
        writer.writeheader()
        lines = 0
        for edge in connections:
            writer.writerow({'nodo_partenza': edge[0].name, 'nodo_arrivo': edge[1].name, 'peso_arco': edge[2]})
            lines = lines + 1
        print("Scritte su file", lines, "righe\n")


def create_connections_from_file(file_name, networkit=False):
    """
    Attraverso tale funzione si rende possibile la creazione di un grafo uguale ad uno precedentemente creato,
    le quali informazioni sono presenti all'interno di un file csv.

    """
    vertices_list = []
    with open('grafi_csv/' + file_name + '.csv', mode='r') as graph_file:
        reader = csv.DictReader(graph_file)
        line_count = 0
        connections = []
        for row in reader:
            if line_count == 0:
                line_count += 1
            vertices_list.append(int(row["nodo_partenza"]))
            vertices_list.append(int(row["nodo_arrivo"]))
            connections.append([int(row["nodo_partenza"]), int(row["nodo_arrivo"]), int(row["peso_arco"])])
            line_count += 1
        print(f'Lette da file {line_count} linee.')
        # gestione nodi isolati
        # dalla generazione del grafo attraverso il metodo ER non è possibile sapere
        # se il grafo creato è connesso
        # vengono considerati tutti i vertici fino al vertice massimo presente nel file di lettura
        if vertices_list:
            m = max(vertices_list)
            vertices_list = [x for x in range(0, m + 1)]
        if not networkit:
            # creazione oggetti Node
            for i in range(len(vertices_list)):
                vertices_list[i] = Node(i)

            for element in connections:
                element[0] = vertices_list[element[0]]
                element[1] = vertices_list[element[1]]

    return connections, vertices_list

