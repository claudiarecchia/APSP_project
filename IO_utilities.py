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
    Attraverso tale funzione si rende possibile la creazione di un grafo uguale ad uno precedentemente creato,
    le quali informazioni sono presenti all'interno di un file csv.
    """
    vertices_list = []
    with open(graph_dir + '/' + file_name + '.csv', mode='r') as graph_file:
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


def create_connections_from_file_real_graph(file_name):
    """
    Attraverso tale funzione si rende possibile la creazione di un grafo uguale ad uno esistente,
    le quali informazioni sono presenti all'interno di un file csv.
    Files reperiti dalla piattaforma https://snap.stanford.edu/index.html
    """
    vertices_list = []
    with open(graph_dir + '/' + file_name + '.csv', mode='r') as graph_file:
        reader = csv.DictReader(graph_file)
        line_count = 0
        connections = []
        # print(reader.fieldnames)

        if "peso_arco" not in reader.fieldnames:
            with open(graph_dir + '/' + file_name + '.csv', mode='w', newline="") as graph_file:
                fieldnames = reader.fieldnames + ["peso_arco"]
                writer = csv.DictWriter(graph_file, fieldnames)
                writer.writeheader()
                for row in reader:
                    row_copy = row
                    row_copy.update({"peso_arco": randint(1, MAX)})
                    writer.writerow(row_copy)
        # print(reader.fieldnames)

        vertices_dict = {}
        count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            if int(row["nodo_partenza"]) not in vertices_list:
                vertices_list.append(int(row["nodo_partenza"]))
                # vertices_dict.update({"nodo": int(row["nodo_partenza"])})
                vertices_dict[int(row["nodo_partenza"])] = int(row["nodo_partenza"])
                count = count+1
            if int(row["nodo_arrivo"]) not in vertices_list:
                vertices_list.append(int(row["nodo_arrivo"]))
                # vertices_dict.update({"nodo": int(row["nodo_arrivo"])})
                vertices_dict[int(row["nodo_arrivo"])] = int(row["nodo_arrivo"])
                count = count+1
            connections.append([int(row["nodo_partenza"]), int(row["nodo_arrivo"]), int(row["peso_arco"])])
            line_count += 1
        print(f'Lette da file {line_count} linee.')
        # print(vertices_dict)
        if vertices_list:
            # ordino la lista
            vertices_list = sorted(vertices_list)
            # creazione oggetti Node
            for i in range(len(vertices_list)):
                # vertices_list[i] = Node(i)
                # vertices_dict[vertices_list[i]] = Node(vertices_list[i])
                # vertices_dict[i] = Node(i)
                vertices_list[i] = Node(vertices_list[i])
                vertices_list[i].set_index(i)

            for element in connections:
                # print(element[0], vertices_list[element[0]], element[1], vertices_list[element[1]] )
                # element[0] = vertices_list[element[0]]
                # element[1] = vertices_list[element[1]]

                # element[0] = vertices_dict.get(element[0])
                # element[1] = vertices_dict.get(element[1])

                element[0] = get_node(vertices_list, element[0])
                element[1] = get_node(vertices_list, element[1])

        return connections, vertices_list


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
