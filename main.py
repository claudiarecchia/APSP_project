
from Dijkstra import *
from Floyd_Warshall import *
from timeit import default_timer as timer


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

    g = GraphAdjMatrix(vertici, connections, directed=False)
    cpu_total = timer()
    for i in range(len(vertici)):
        # print("ESECUZIONE ", i)
        dijkstra(g, g.get_nodo(i))
        shortest(g, g.get_nodo(i))
        for vertex in vertici:
            vertex.reset_properties(vertex.name)

    time = round(timer() - cpu_total, 6)
    print("TEMPO CPU TOTALE APSP DIJKSTRA MATRICE DI ADIACENZA:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")

###############################################################################################################
    g = GraphAdjList(vertici, connections, directed=False)
    cpu_total = timer()
    for i in range(len(vertici)):
        # print("ESECUZIONE ", i)
        dijkstra(g, g.get_nodo(i))
        shortest(g, g.get_nodo(i))
        for vertex in vertici:
            vertex.reset_properties(vertex.name)

    time = round(timer() - cpu_total, 6)
    print("TEMPO CPU TOTALE APSP DIJKSTRA LISTE DI ADIACENZA:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")

###############################################################################################################

    g = GraphAdjMatrix(vertici, connections, directed=False)
    cpu_total = timer()
    floyd_warshall(g)
    time = round(timer() - cpu_total, 6)
    print("TEMPO CPU TOTALE APSP FLOYD-WARSHALL:", time,
          "\n/////////////////////////////////////////////////////////////////////////////\n\n")
