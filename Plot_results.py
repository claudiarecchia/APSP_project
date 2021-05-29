import matplotlib.pyplot as plt
from IO_utilities import *

executions = get_values_from_results()
graph_type = ["g_BA", "g_ER_p01", "g_ER_p05", "g_ER_p1", "path", "p2p-Gnutella08", "p2p-Gnutella08", "p2p-Gnutella08",
              "soc-sign-bitcoinalpha"]
i = 0

density_list = []

def plot_result():
    if val == 0:
        plt.plot(num_nodes, ex_time, 'b', marker='o', label='Dijkstra')
        plt.plot(num_nodes_dp, ex_time_dp, 'g', marker='o', linestyle='--', label='Dijkstra parallelo')
        plt.plot(num_nodes_f, ex_time_f, 'r', marker='o', label='Floyd-Warshall')
        plt.xlabel('Numero nodi')

    else:
        plt.plot(num_edges, ex_time, 'b', marker='o', label='Dijkstra')
        plt.plot(num_edges_dp, ex_time_dp, 'g', marker='o', linestyle='--', label='Dijkstra parallelo')
        plt.plot(num_edges_f, ex_time_f, 'r', marker='o', label='Floyd-Warshall')
        plt.xlabel('Numero archi')
    if graph_type[i] == "g_BA":
        plt.title("Barabasi-Albert")
    if graph_type[i] == "g_ER_p01":
        plt.title("Erdos-Renyi p=0.1")
    if graph_type[i] == "g_ER_p05":
        plt.title("Erdos-Renyi p=0.5")
    if graph_type[i] == "g_ER_p1":
        plt.title("Erdos-Renyi p=1")
    if graph_type[i] == "path":
        plt.title("Grafo a path")
    if graph_type[i] == "p2p-Gnutella08":
        plt.title("Grafo reale: p2p-Gnutella08")
    if graph_type[i] == "p2p-Gnutella08":
        plt.title("Grafo reale: p2p-Gnutella08")
    if graph_type[i] == "p2p-Gnutella08":
        plt.title("Grafo reale: p2p-Gnutella08")
    if graph_type[i] == "soc-sign-bitcoinalpha":
        plt.title("Grafo reale: soc-sign-bitcoinalpha")
    plt.ylabel('Tempo di esecuzione')
    plt.legend()
    plt.show()


for graph in graph_type:
    ex_time = []
    num_nodes = []
    num_edges = []
    density = []
    ex_time_f = []
    num_nodes_f = []
    num_edges_f = []
    ex_time_dp = []
    num_nodes_dp = []
    num_edges_dp = []
    for ex in executions:
        if graph_type[i] in ex[0]:
            if "F" in ex[1]:
                ex_time_f.append(float(ex[2]))  # tempo di esecuzione
                num_nodes_f.append(float(ex[3]))  # n_nodi
                num_edges_f.append(ex[4])  # n_edges
            elif "DP" in ex[1]:
                ex_time_dp.append(float(ex[2]))  # tempo di esecuzione
                num_nodes_dp.append(float(ex[3]))  # n_nodi
                num_edges_dp.append(ex[4])  # n_edges
            elif "D" in ex[1]:
                ex_time.append(float(ex[2]))  # tempo di esecuzione
                density.append(float(ex[5]))  # indice di densità
                num_nodes.append(float(ex[3]))  # n_nodi
                num_edges.append(ex[4])  # n_edges

        density_list.append([ex[0], density, ex_time])

    for val in [0, 1]:
        plot_result()
    i += 1

# density_dijkstra_125 = []
# time_dijkstra_125 = []
# density_dijkstra_250 = []
# time_dijkstra_250 = []
# density_dijkstra_500 = []
# time_dijkstra_500 = []
# density_dijkstra_1000 = []
# time_dijkstra_1000 = []
# density_dijkstra_2000 = []
# time_dijkstra_2000 = []
#
# for element in density_list:
#     print(element[0])
#     if element[0] == "g_ER_p01_125" or element[0] == "g_ER_p05_125" or element[0] == "g_ER_p1_125":
#         density_dijkstra_125.append(element[1])
#         time_dijkstra_125.append(element[2])
#
#     if element[0] == "g_ER_p01_250" or element[0] == "g_ER_p05_250" or element[0] == "g_ER_p1_250":
#         density_dijkstra_250.append(element[1])
#         time_dijkstra_250.append(element[2])
#
#     if element[0] == "g_ER_p01_500" or element[0] == "g_ER_p05_500" or element[0] == "g_ER_p1_500":
#         density_dijkstra_500.append(element[1])
#         time_dijkstra_500.append(element[2])
#
#     if element[0] == "g_ER_p01_1000" or element[0] == "g_ER_p05_1000" or element[0] == "g_ER_p1_1000":
#         density_dijkstra_1000.append(element[1])
#         time_dijkstra_1000.append(element[2])
#
#     if element[0] == "g_ER_p01_2000" or element[0] == "g_ER_p05_2000" or element[0] == "g_ER_p1_2000":
#         density_dijkstra_2000.append(element[1])
#         time_dijkstra_2000.append(element[2])
#
#
# plt.plot(density_dijkstra_2000, time_dijkstra_2000, 'b', marker='o', label='2000 nodi')
# plt.title("Relazione tempo esecuzione/indice di densità per l'algoritmo di Dijkstra")
# plt.ylabel('Tempo di esecuzione')
# plt.xlabel('Indice di densità del grafo')
# plt.legend()
# plt.show()