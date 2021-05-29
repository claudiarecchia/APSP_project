"""
In questo file è presente una funzione utile per la creazione di un grafo in maniera randomica,
sfruttando il modello Erdős–Rényi (basato sulle variabili globali m, b, a)
"""

import time
import csv
from random import *
from FibHeap import *
from Global_variables import *


def write_connections_to_file(connections, file_name):
    """
    Nel caso in cui nell'algoritmo di Dijkstra o Floyd-Warshall venga creato un nuovo grafo,
    attraverso tale funzione è possibile rendere replicabile l'esecuzione dell'esperimento
    trascrivendo su un file il grafo generato
    """
    with open(graph_dir + '/' + file_name + '.csv', mode='w') as graph_file:
        fieldnames = ['nodo_partenza', 'nodo_arrivo', 'peso_arco']
        writer = csv.DictWriter(graph_file, fieldnames=fieldnames)
        writer.writeheader()
        lines = 0
        # nel caso in cui gli edge siano oggi Node (nel caso di creazione con Barabasi-Albert mediante networkit)
        if not(isinstance(connections[0][0], int)):
            for edge in connections:
                writer.writerow({'nodo_partenza': edge[0].name, 'nodo_arrivo': edge[1].name, 'peso_arco': edge[2]})
                lines = lines + 1
        else:
            for edge in connections:
                writer.writerow({'nodo_partenza': edge[0], 'nodo_arrivo': edge[1], 'peso_arco': edge[2]})
                lines = lines + 1
        print("Scritte su file", lines, "righe\n")


def create_connections_from_file(file_name, networkit=False):
    """
    Attraverso tale funzione si rende possibile la creazione di un grafo uguale ad uno esistente,
    le quali informazioni sono presenti all'interno di un file csv.
    Funzione valida sia per i grafi generati mediante i metodi di ER, BA, sia per grafi a path e per grafi reali,
    reperiti dalla piattaforma https://snap.stanford.edu/index.html
    """
    vertices_list = []
    with open(graph_dir + '/' + file_name + '.csv', mode='r') as graph_file:
        reader = csv.DictReader(graph_file)
        line_count = 0
        connections = []
        if "peso_arco" not in reader.fieldnames:
            add_weights(file_name, reader)
            with open(graph_dir + '/' + file_name + '.csv', mode='r') as graph_file:
                reader = csv.DictReader(graph_file)
                vertices_list = read_file(connections, line_count, reader, vertices_list, networkit)
        else:
            vertices_list = read_file(connections, line_count, reader, vertices_list, networkit)
        return connections, vertices_list


def read_file(connections, line_count, reader, vertices_list, networkit):
    vertices_dict = {}
    count = 0
    for row in reader:
        if line_count == 0:
            line_count += 1
        if int(row["nodo_partenza"]) not in vertices_list:
            vertices_list.append(int(row["nodo_partenza"]))
            vertices_dict[int(row["nodo_partenza"])] = int(row["nodo_partenza"])
            count = count + 1
        if int(row["nodo_arrivo"]) not in vertices_list:
            vertices_list.append(int(row["nodo_arrivo"]))
            vertices_dict[int(row["nodo_arrivo"])] = int(row["nodo_arrivo"])
            count = count + 1
        connections.append([int(row["nodo_partenza"]), int(row["nodo_arrivo"]), int(row["peso_arco"])])
        line_count += 1
    print(f'Lette da file {line_count} linee.')
    if vertices_list:
        # ordino la lista
        vertices_list = sorted(vertices_list)
        # creazione oggetti Node
        if not networkit:
            for i in range(len(vertices_list)):
                vertices_list[i] = Node(vertices_list[i])
                vertices_list[i].set_index(i)
            for element in connections:
                element[0] = get_node(vertices_list, element[0])
                element[1] = get_node(vertices_list, element[1])
    return vertices_list


def add_weights(file_name, reader):
    with open(graph_dir + '/' + file_name + '.csv', mode='w') as graph_file:
        fieldnames = reader.fieldnames + ["peso_arco"]
        writer = csv.DictWriter(graph_file, fieldnames)
        writer.writeheader()
        for row in reader:
            row_copy = row
            row_copy.update({"peso_arco": randint(1, MAX)})
            writer.writerow(row_copy)



def get_node(lista_vertici, element):
    for el in lista_vertici:
        if el.name == element:
            return el


def report_exec_time(graph_file_name, algo, running_time, num_nodes, num_edges, density_index):
    """
    Funzione utilizzata per raccogliere i dati delle varie esecuzioni degli algoritmi
    in un file .csv, in modo tale da poter essere successivamente letto
    per effettuarne una rappresentazione grafica mediante un plot
    """
    with open(report_dir + '/' + report_file + '.csv', 'a') as report:
        fieldnames = ['graph_name', 'algo', 'running_time', 'num_nodes', 'num_edges', 'density_index']
        writer = csv.DictWriter(report, fieldnames=fieldnames)
        writer.writerow({'graph_name': graph_file_name, 'algo': algo, 'running_time': running_time,
                         'num_nodes': num_nodes, 'num_edges': num_edges, 'density_index': density_index})


def get_values_from_results():
    """
    Attraverso tale funzione si rende possibile il reperimento delle informazioni salvate sul file .csv relativo
    ai risultati ottenuti dalle varie sperimentazioni
    """
    values = []
    with open(report_dir + '/' + report_file + '.csv', mode='r') as result_file:
        reader = csv.DictReader(result_file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            values.append([row["graph_name"], row["algo"], row["running_time"],
                           row["num_nodes"], row["num_edges"], row["density_index"]])
            line_count += 1
        print(f'Lette da file {line_count} linee.')
        # for el in values:
        #     print(el)
    return values
