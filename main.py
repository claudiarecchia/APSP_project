from Dijkstra import *
from Floyd_Warshall import *
from timeit import default_timer as timer
from Global_variables import *
import networkit as nk
import multiprocessing as mp
import psutil
from Graphs_generators import *
import os
import networkx as nx
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def execute_with_networkit(file_name):
    """
    Utilizzo le funzioni di networkit per verificare la correttezza degli algoritmi implementati.
    Networkit fornisce lo stesso risultato degli algoritmi solamente nel caso in cui il grafo sia diretto (DIR=True)
    poichè nella funzione addEdge di nk.Graph "It is not checked whether this edge already exists, thus it is possible
    to create multi-edges.", il quale controllo invece viene effettuato nelle implementazioni realizzate,
    presenti nel file Graph.py
    """
    conn, ver = create_connections_from_file(file_name, networkit=True)
    g = nk.Graph(n=max(ver) + 1, weighted=True, directed=True)
    for tupla in conn:
        g.addEdge(tupla[0], tupla[1], tupla[2])
    dist = nk.distance.APSP(g)
    dist.run()
    matrix = dist.getDistances()
    for riga in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[riga][col] > sys.maxsize / 2:
                matrix[riga][col] = sys.maxsize  # per avere uguaglianza con Floyd-Warshall e Dijkstra
            else:
                matrix[riga][col] = int(matrix[riga][col])
    mat = create_square_matrix(ver)
    for i in range(len(ver)):
        for j in range(len(ver)):
            if i != j:
                mat[i][j] = matrix[ver[i]][ver[j]]
    return mat


def create_square_matrix(ver):
    mat = []
    for i in range(len(ver)):
        list = []
        for j in range(len(ver)):
            list.append(0)
        mat.append(list)
    return mat


def execute_FloydWarshall(vertici, connections):
    g = GraphAdjMatrix(vertici, connections, directed=DIR)
    cpu_total = timer()
    mat = floyd_warshall(g)
    time = round(timer() - cpu_total, 6)
    return time, mat


def execute_Dijkstra_APSP(vertici, connections, check):
    g = GraphAdjList(vertici, connections, directed=DIR)
    mat = create_square_matrix(vertici)
    if not check:
        cpu_total = timer()
        for i in range(len(vertici)):
            dijkstra(g, g.get_node(i))
            for vertex in vertici:
                vertex.reset_properties(vertex.name, vertex.index)
        time = round(timer() - cpu_total, 6)
    else:
        cpu_total = timer()
        for i in range(len(vertici)):
            dijkstra(g, g.get_node(i))
            shortest(g, g.get_node(i), mat)
            for vertex in vertici:
                vertex.reset_properties(vertex.name, vertex.index)
        time = round(timer() - cpu_total, 6)
    return time, mat


def exec_dijkstra(grafo, num_nodo):
    dijkstra(grafo, grafo.get_node(num_nodo))
    for v in grafo.vertici:
        v.reset_properties(v.name)


def execute_Dijkstra_APSP_parallel(vertici, connections):
    g = GraphAdjList(vertici, connections, directed=DIR)
    process_creation = 0
    cpu_total = timer()
    jobs = []
    for i in range(len(vertici)):
        process_creation_begin = timer()
        p = mp.Process(target=exec_dijkstra, args=(g, i))
        process_creation_end = timer()
        jobs.append(p)
        process_creation = process_creation + (process_creation_end - process_creation_begin)
        p.start()
    for job in jobs:
        job.join()
        job.close()
    time = round(timer() - cpu_total, 6)
    values = psutil.cpu_percent(percpu=True)
    print("Valori percentuali CPU:", values)
    print("Tempo totale per la creazione dei processi:", process_creation)
    return time


if __name__ == '__main__':
    value = int(input("Creare un nuovo grafo (1) o usare un file per la lettura (2) ?:\n"))
    if value == 1:
        file_name = (input("Inserire nome file di scrittura del nuovo grafo:\n"))
        n = int(input("Inserire il numero di vertici del grafo:\n"))
        vertici = []
        for i in range(n):
            vertici.append(Node(i))
        graph_type = int(input("Creare un grafo sul modello ER (1), un grafo a path (2) o un grafo con modello Barabasi-Albert (3) ?:\n"))
        if graph_type == 1:
            connections = create_ER_graph(vertici, m, file_name)
        elif graph_type == 2:
            connections = create_path_graph(vertici, file_name)
        elif graph_type == 3:
            connections, vertici = create_barabasi_albert_graph(n, file_name)
        else:
            raise IOError('Valore fornito non ammesso')
    elif value == 2:
        file_name = (input("Inserire nome file di lettura del grafo:\n"))
        connections, vertici = create_connections_from_file(file_name)
    else:
        raise IOError('Valore fornito non ammesso')
    assert connections, "Il grafo è vuoto"
    # calcolo indice di densità del grafo
    if DIR:
        # L / n(n - 1)
        index = (len(connections) - 1) / (len(vertici) * (len(vertici) - 1))
    else:
        index = (2 * (len(connections) - 1)) / (len(vertici) * (len(vertici) - 1))

    time, mat_f = execute_FloydWarshall(vertici, connections)
    report_exec_time(file_name, "F", time, len(vertici), len(connections), index)

    time, mat_d = execute_Dijkstra_APSP(vertici, connections, check)
    report_exec_time(file_name, "D", time, len(vertici), len(connections), index)

    execute_Dijkstra_APSP_parallel(vertici, connections)
    report_exec_time(file_name, "DP", time, len(vertici), len(connections), index)
    if DIR:
        mat_nk = execute_with_networkit(file_name)
        if check:
            for riga in range(len(mat_f)):
                for col in range(len(mat_f)):
                    assert mat_f[riga][col] == mat_d[riga][col] \
                           or mat_f[riga][col] == mat_nk[riga][col], "ERRORE: i cammini minimi non risultano essere uguali"
