
from Dijkstra import *
from Floyd_Warshall import *
from timeit import default_timer as timer
from Global_variables import *
import networkit as nk
import multiprocessing as mp
import psutil

def execute_with_networkit(file_name):
    """
    Utilizzo le funzioni di networkit per verificare la correttezza degli algoritmi implementati.
    Networkit fornisce lo stesso risultato degli algoritmi solamente nel caso in cui il grafo sia diretto (DIR=True)
    poichè nella funzione addEdge di nk.Graph "It is not checked whether this edge already exists, thus it is possible
    to create multi-edges.", il quale controllo invece viene effettuato nelle implementazioni realizzate,
    presenti nel file Grafo.py
    """
    print("APSP DIJKSTRA NETWORKIT:\n")
    connections, vertici = create_connections_from_file(file_name, networkit=True)
    g = nk.Graph(n=len(vertici), weighted=True, directed=True)
    for tupla in connections:
        g.addEdge(tupla[0], tupla[1], tupla[2])
    dist = nk.distance.APSP(g)
    dist.run()
    matrix = dist.getDistances()
    for riga in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[riga][col] > sys.maxsize / 2:
                matrix[riga][col] = "INF"
            else:
                matrix[riga][col] = int(matrix[riga][col])
    n_elements = []
    for i in range(len(vertici)): n_elements.append(i)
    print_nice = pd.DataFrame(matrix, index=n_elements, columns=n_elements)
    print(print_nice)


def execute_FloydWarshall(vertici, connections):
    g = GraphAdjMatrix(vertici, connections, directed=DIR)
    cpu_total = timer()
    floyd_warshall(g)
    time = round(timer() - cpu_total, 6)
    print("TEMPO CPU TOTALE APSP FLOYD-WARSHALL:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")


def execute_Dikstra_APSP(vertici, connections, adj_list):
    if adj_list:
        g = GraphAdjList(vertici, connections, directed=DIR)
    else:
        g = GraphAdjMatrix(vertici, connections, directed=DIR)

    cpu_total = timer()
    for i in range(len(vertici)):
        dijkstra(g, g.get_nodo(i))
        # shortest(g, g.get_nodo(i))
        for vertex in vertici:
            vertex.reset_properties(vertex.name)
    time = round(timer() - cpu_total, 6)

    values = psutil.cpu_percent(percpu=True)
    print("Valori percentuali CPU:", values)

    if adj_list:
        print("TEMPO CPU TOTALE APSP DIJKSTRA LISTE DI ADIACENZA:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n")
    else:
        print("TEMPO CPU TOTALE APSP DIJKSTRA MATRICE DI ADIACENZA:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n")


def exec_dijkstra(grafo, num_nodo):
    dijkstra(grafo, grafo.get_nodo(num_nodo))
    # shortest(grafo, grafo.get_nodo(num_nodo))
    for v in grafo.vertici:
        v.reset_properties(v.name)


def execute_Dikstra_APSP_parallel(vertici, connections, adj_list):
    if adj_list:
        g = GraphAdjList(vertici, connections, directed=DIR)
    else:
        g = GraphAdjMatrix(vertici, connections, directed=DIR)

    num_cores = mp.cpu_count()
    print("num cores: ", num_cores)

    cpu_total = timer()

    jobs = []
    for i in range(len(vertici)):
        p = mp.Process(target=exec_dijkstra, args=(g, i))
        jobs.append(p)
        p.start()

    time = round(timer() - cpu_total, 6)
    values = psutil.cpu_percent(percpu=True)
    print("Valori percentuali CPU:", values)

    if adj_list:
        print("TEMPO CPU TOTALE APSP DIJKSTRA LISTE DI ADIACENZA PARALLELO:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n")
    else:
        print("TEMPO CPU TOTALE APSP DIJKSTRA MATRICE DI ADIACENZA PARALLELO:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n")


if __name__ == '__main__':
    value = int(input("Creare un nuovo grafo (1) o usare un file per la lettura (2) ?:\n"))

    if value == 1:
        file_name = (input("Inserire nome file di scrittura del nuovo grafo:\n"))
        n = int(input("Inserire il numero di vertici del grafo:\n"))
        vertici = []
        for i in range(n):
            vertici.append(Node(i))

        graph_type = int(input("Creare un grafo sul modello ER (1) o un grafo a path (2) ?:\n"))
        if graph_type == 1:
            connections = create_ER_graph(vertici, m, file_name)
        elif graph_type == 2:
            connections = create_path_graph(vertici, file_name)
        else:
            raise IOError('Valore fornito non ammesso')

    elif value == 2:
        file_name = (input("Inserire nome file di lettura del grafo:\n"))
        connections, vertici = create_connections_from_file(file_name)
    else:
        raise IOError('Valore fornito non ammesso')

    assert connections, "Il grafo è vuoto"

    execute_Dikstra_APSP(vertici, connections, adj_list=False)

    execute_Dikstra_APSP(vertici, connections, adj_list=True)

    execute_FloydWarshall(vertici, connections)

    execute_Dikstra_APSP_parallel(vertici, connections, adj_list=True)

    if DIR:
        execute_with_networkit(file_name)
