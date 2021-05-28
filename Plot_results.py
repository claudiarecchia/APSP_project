import matplotlib.pyplot as plt
from IO_utilities import *


executions = get_values_from_results()

ex_time = []
num_nodes = []
num_edges = []
ex_time_f = []
num_nodes_f = []
num_edges_f = []
ex_time_d_er01 = []
num_nodes_d_er01 = []
num_edges_d_er01 = []
ex_time_f_er01 = []
um_nodes_f_er01 = []
num_edges_f_er01 = []
ex_time_d_er05 = []
num_nodes_d_er05 = []
num_edges_d_er05 = []
ex_time_f_er05 = []
um_nodes_f_er05 = []
num_edges_f_er05 = []
ex_time_d_er1 = []
num_nodes_d_er1 = []
num_edges_d_er1 = []
ex_time_f_er1 = []
um_nodes_f_er1 = []
num_edges_f_er1 = []
ex_time_d_path = []
num_nodes_d_path = []
num_edges_d_path = []
ex_time_f_path = []
um_nodes_f_path = []
num_edges_f_path = []

density_dijkstra_125 = []
time_dijkstra_125 = []
density_dijkstra_250 = []
time_dijkstra_250 = []
density_dijkstra_500 = []
time_dijkstra_500 = []
density_dijkstra_1000 = []
time_dijkstra_1000 = []
density_dijkstra_2000 = []
time_dijkstra_2000 = []

for ex in executions:
    if "BA" in ex[0]:
        if "D" in ex[1]:
            ex_time.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            num_nodes.append(float(ex[3]))  # n_nodi
            num_edges.append(ex[4])  # n_edges
        elif "F" in ex[1]:
            ex_time_f.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            num_nodes_f.append(float(ex[3]))  # n_nodi
            num_edges_f.append(ex[4])   # n_edges

    if "ER_p01" in ex[0]:
        if "D" in ex[1]:
            ex_time_d_er01.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            num_nodes_d_er01.append(float(ex[3]))  # n_nodi
            num_edges_d_er01.append(ex[4])   # n_edges
        elif "F" in ex[1]:
            ex_time_f_er01.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            um_nodes_f_er01.append(float(ex[3]))  # n_nodi
            num_edges_f_er01.append(ex[4])   # n_edges

    if "ER_p05" in ex[0]:
        if "D" in ex[1]:
            ex_time_d_er05.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            num_nodes_d_er05.append(float(ex[3]))  # n_nodi
            num_edges_d_er05.append(ex[4])   # n_edges
        elif "F" in ex[1]:
            ex_time_f_er05.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            um_nodes_f_er05.append(float(ex[3]))  # n_nodi
            num_edges_f_er05.append(ex[4])   # n_edges

    if "ER_p1" in ex[0]:
        if "D" in ex[1]:
            ex_time_d_er1.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            num_nodes_d_er1.append(float(ex[3]))  # n_nodi
            num_edges_d_er1.append(ex[4])   # n_edges
        elif "F" in ex[1]:
            ex_time_f_er1.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            um_nodes_f_er1.append(float(ex[3]))  # n_nodi
            num_edges_f_er1.append(ex[4])   # n_edges

    if "path" in ex[0]:
        if "D" in ex[1]:
            ex_time_d_path.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            num_nodes_d_path.append(float(ex[3]))  # n_nodi
            num_edges_d_path.append(ex[4])   # n_edges

        elif "F" in ex[1]:
            ex_time_f_path.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            um_nodes_f_path.append(float(ex[3]))  # n_nodi
            num_edges_f_path.append(ex[4])   # n_edges

    if (ex[0] == "g_ER_p01_125" or ex[0] == "g_ER_p05_125" or ex[0] == "g_ER_p1_125") and ("D" in ex[1]):
        density_dijkstra_125.append(ex[5])
        time_dijkstra_125.append(float(ex[2]))

    if (ex[0] == "g_ER_p01_250" or ex[0] == "g_ER_p05_250" or ex[0] == "g_ER_p1_250") and ("D" in ex[1]):
        density_dijkstra_250.append(ex[5])
        time_dijkstra_250.append(float(ex[2]))

    if (ex[0] == "g_ER_p01_500" or ex[0] == "g_ER_p05_500" or ex[0] == "g_ER_p1_500") and ("D" in ex[1]):
        density_dijkstra_500.append(ex[5])
        time_dijkstra_500.append(float(ex[2]))

    if (ex[0] == "g_ER_p01_1000" or ex[0] == "g_ER_p05_1000" or ex[0] == "g_ER_p1_1000") and ("D" in ex[1]):
        density_dijkstra_1000.append(ex[5])
        time_dijkstra_1000.append(float(ex[2]))

    if (ex[0] == "g_ER_p01_2000" or ex[0] == "g_ER_p05_2000" or ex[0] == "g_ER_p1_2000") and ("D" in ex[1]):
        density_dijkstra_2000.append(ex[5])
        time_dijkstra_2000.append(float(ex[2]))

#####################################################################
plt.plot(num_nodes, ex_time, 'b', marker='o', label='Dijkstra')
plt.plot(num_nodes_f, ex_time_f, 'r', marker='o', label='Floyd-Warshall')
plt.title("Barabasi-Albert")
plt.ylabel('Tempo di esecuzione')
# plt.ylabel('Indice di densità')
plt.xlabel('Numero nodi ')
plt.legend()
plt.show()

plt.plot(num_edges, ex_time, 'b', marker='o', label='Dijkstra')
plt.plot(num_edges_f, ex_time_f, 'r', marker='o', label='Floyd-Warshall')
plt.title("Barabasi-Albert")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero archi')
plt.legend()
plt.show()
#####################################################################
plt.plot(num_nodes_d_er01, ex_time_d_er01, 'b', marker='o', label='Dijkstra')
plt.plot(um_nodes_f_er01, ex_time_f_er01, 'r', marker='o', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=0.1")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero nodi')
plt.legend()
plt.show()

plt.plot(num_edges_d_er01, ex_time_d_er01, 'b', marker='o', label='Dijkstra')
plt.plot(num_edges_f_er01, ex_time_f_er01, 'r', marker='o', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=0.1")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero archi')
plt.legend()
plt.show()
#####################################################################
plt.plot(num_nodes_d_er05, ex_time_d_er05, 'b', marker='o', label='Dijkstra')
plt.plot(um_nodes_f_er05, ex_time_f_er05, 'r', marker='o', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=0.5")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero nodi')
plt.legend()
plt.show()

plt.plot(num_edges_d_er05, ex_time_d_er05, 'b', marker='o', label='Dijkstra')
plt.plot(num_edges_f_er05, ex_time_f_er05, 'r', marker='o', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=0.5")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero archi')
plt.legend()
plt.show()
#####################################################################
plt.plot(num_nodes_d_er1, ex_time_d_er1, 'b', marker='o', label='Dijkstra')
plt.plot(um_nodes_f_er1, ex_time_f_er1, 'r', marker='o', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=1")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero nodi')
plt.legend()
plt.show()

plt.plot(num_edges_d_er1, ex_time_d_er1, 'b', marker='o', label='Dijkstra')
plt.plot(num_edges_f_er1, ex_time_f_er1, 'r', marker='o', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=1")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero archi')
plt.legend()
plt.show()
#####################################################################
plt.plot(num_nodes_d_path, ex_time_d_path, 'b', marker='o', label='Dijkstra')
plt.plot(um_nodes_f_path, ex_time_f_path, 'r', marker='o', label='Floyd-Warshall')
plt.title("Grafo a path")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero nodi')
plt.legend()
plt.show()

plt.plot(num_edges_d_path, ex_time_d_path, 'b', marker='o', label='Dijkstra')
plt.plot(num_edges_f_path, ex_time_f_path, 'r', marker='o', label='Floyd-Warshall')
plt.title("Grafo a path")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Numero archi')
plt.legend()
plt.show()
#####################################################################
plt.plot(density_dijkstra_125, time_dijkstra_125, 'b', marker='o', label='125 nodi')
plt.title("Relazione tempo esecuzione/indice di densità per l'algoritmo di Dijkstra")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Indice di densità del grafo')
plt.legend()
plt.show()
#####################################################################
plt.plot(density_dijkstra_250, time_dijkstra_250, 'y', marker='o', label='250 nodi')
plt.title("Relazione tempo esecuzione/indice di densità per l'algoritmo di Dijkstra")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Indice di densità del grafo')
plt.legend()
plt.show()
#####################################################################
plt.plot(density_dijkstra_500, time_dijkstra_500, 'g', marker='o', label='500 nodi')
plt.title("Relazione tempo esecuzione/indice di densità per l'algoritmo di Dijkstra")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Indice di densità del grafo')
plt.legend()
plt.show()
#####################################################################
plt.plot(density_dijkstra_1000, time_dijkstra_1000, 'r', marker='o', label='1000 nodi')
plt.title("Relazione tempo esecuzione/indice di densità per l'algoritmo di Dijkstra")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Indice di densità del grafo')
plt.legend()
plt.show()
#####################################################################
plt.plot(density_dijkstra_2000, time_dijkstra_2000, 'b', marker='o', label='2000 nodi')
plt.title("Relazione tempo esecuzione/indice di densità per l'algoritmo di Dijkstra")
plt.ylabel('Tempo di esecuzione')
plt.xlabel('Indice di densità del grafo')
plt.legend()
plt.show()
