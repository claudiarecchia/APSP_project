"""
In questo file è presente una funzione utile per la creazione di un grafo in maniera randomica,
sfruttando il modello Erdős–Rényi (basato sulle variabili globali m, b, a)
"""

import time
import csv
from random import *
from FibHeap import *

MAX = 50
m = 2 ** 32
b = 12345
a = 1103515245

new_vertici = []


def rng(M=m, A=a, B=b):
    rng.current = (A * rng.current + B) % M
    return rng.current


def create_ER_graph(vertici, m, file_name):
    """ Creazione di un grafo in maniera randomica secondo il modello ER """
    rng.current = int(round(time.time() * 1000))
    p = 0.45  # probabilità
    connections = []
    for i in vertici:
        for j in vertici:
            if round(rng(m) / m) > p:
                if i != j:  # no self-loop
                    peso = randint(1, MAX)
                    connections.append((i, j, peso))
    write_connections_to_file(connections, file_name)
    return connections


def write_connections_to_file(connections, file_name):
    """
    Nel caso in cui nell'algoritmo di Dijkstra o Floyd-Warshall venga creato un nuovo grafo,
    attraverso tale funzione è possibile rendere replicabile l'esecuzione dell'algoritmo
    trascrivendo su un file il grafo generato
    """
    with open('grafi_csv/' + file_name + '.csv', mode='w') as graph_file:
        fieldnames = ['nodo_partenza', 'nodo_arrivo', 'peso_arco']
        writer = csv.DictWriter(graph_file, fieldnames=fieldnames)
        writer.writeheader()
        for edge in connections:
            writer.writerow({'nodo_partenza': edge[0].name, 'nodo_arrivo': edge[1].name, 'peso_arco': edge[2]})


def create_connections_from_file(file_name):
    """
    Attraverso tale funzione si rende possibile la creazione di un grafo uguale ad uno precedentemente creato,
    le quali informazioni sono presenti all'interno di un file csv.
    """
    connections = []
    with open('grafi_csv/' + file_name + '.csv', mode='r') as graph_file:
        reader = csv.DictReader(graph_file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                # print(f'I nomi delle colonne sono {", ".join(row)}')
                line_count += 1
            # print(f' ( \t{row["nodo_partenza"]} , {row["nodo_arrivo"]} , {row["peso_arco"]} )')
            nodo_p, nodo_a = get_nodes(int(row["nodo_partenza"]), int(row["nodo_arrivo"]))
            connections.append([nodo_p, nodo_a, int(row["peso_arco"])])
            line_count += 1
        print(f'Processed {line_count} lines.')
    return connections, new_vertici


def get_nodes(nodo_partenza, nodo_arrivo):
    """
    Attraverso questa funzione è possibile ottenere gli oggetti nodo richiesti,
    creandoli se non ancora esistenti o riconducendosi agli elementi precedentemente creati
    """
    create_p = True
    create_a = True
    nodo_p = Node(nodo_partenza)
    nodo_a = Node(nodo_arrivo)
    if not new_vertici:
        new_vertici.append(nodo_p)
        if nodo_partenza != nodo_arrivo:  # se sono permessi self-loops
            new_vertici.append(nodo_a)
    else:
        for vertex in new_vertici:
            if nodo_partenza == vertex.name:
                create_p = False
                nodo_p = vertex
            if nodo_arrivo == vertex.name:
                create_a = False
                nodo_a = vertex
        if create_p: new_vertici.append(nodo_p)
        if create_a: new_vertici.append(nodo_a)
    return nodo_p, nodo_a
