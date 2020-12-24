
from Dijkstra import *
from Floyd_Warshall import *
from timeit import default_timer as timer
from Global_variables import *
import networkit as nk


def execute_with_networkit():
    global connections, vertici, g, i
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


def execute_with_FW():
    global g, cpu_total, time
    g = GraphAdjMatrix(vertici, connections, directed=DIR)
    cpu_total = timer()
    floyd_warshall(g)
    time = round(timer() - cpu_total, 6)
    print("TEMPO CPU TOTALE APSP FLOYD-WARSHALL:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")


def execute_Dikstra_APSP(vertici, connections, adj_list):
    global g, cpu_total, i, vertex, time
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
    if adj_list:
        print("TEMPO CPU TOTALE APSP DIJKSTRA LISTE DI ADIACENZA:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")
    else:
        print("TEMPO CPU TOTALE APSP DIJKSTRA MATRICE DI ADIACENZA:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")


if __name__ == '__main__':
    value = int(input("Creare un nuovo grafo (1) o usare un file per la lettura (2) ?:\n"))

    if value == 1:
        file_name = (input("Inserire nome file di scrittura del nuovo grafo:\n"))
        n = int(input("Inserire il numero di vertici del grafo:\n"))
        vertici = []
        for i in range(n):
            vertici.append(Node(i))
        connections = create_ER_graph(vertici, m, file_name)
    elif value == 2:
        file_name = (input("Inserire nome file di lettura del grafo:\n"))
        connections, vertici = create_connections_from_file(file_name)
    else:
        raise IOError('Valore fornito non ammesso')

    assert connections, "Il grafo è vuoto"

    execute_Dikstra_APSP(vertici, connections, adj_list=False)

    execute_Dikstra_APSP(vertici, connections, adj_list=True)

    execute_with_FW()

    execute_with_networkit()
