import matplotlib.pyplot as plt
from IO_utilities import *

executions = get_values_from_results()
graph_type = ["g_BA", "g_ER_p01", "g_ER_p05", "g_ER_p1", "path", "p2p-Gnutella08", "facebook_combined", "Wiki-Vote",
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
    if graph_type[i] == "facebook_combined":
        plt.title("Grafo reale: facebook_combined")
    if graph_type[i] == "Wiki-Vote":
        plt.title("Grafo reale: Wiki-Vote")
    if graph_type[i] == "soc-sign-bitcoinalpha":
        plt.title("Grafo reale: soc-sign-bitcoinalpha")
    plt.ylabel('Tempo di esecuzione')
    plt.legend()
    plt.show()

dijkstra = []
floyd = []

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
                floyd.append([ex[0], float(ex[2]), ex[3], ex[4], float(ex[5])])
            elif "DP" in ex[1]:
                ex_time_dp.append(float(ex[2]))  # tempo di esecuzione
                num_nodes_dp.append(float(ex[3]))  # n_nodi
                num_edges_dp.append(ex[4])  # n_edges
            elif "D" in ex[1]:
                ex_time.append(float(ex[2]))  # tempo di esecuzione
                density.append(float(ex[5]))  # indice di densità
                num_nodes.append(float(ex[3]))  # n_nodi
                num_edges.append(ex[4])  # n_edges
                # nome, ex_time, n_nodi, n_edges, density
                dijkstra.append([ex[0], float(ex[2]), ex[3], ex[4], float(ex[5])])

        density_list.append([ex[0], density, ex_time])

    for val in [0, 1]:
        plot_result()
        pass
    i += 1

plt.plot(dijkstra[4][4], dijkstra[4][1], 'b', marker='o', label=dijkstra[4][0])
plt.plot(dijkstra[9][4], dijkstra[9][1], 'y', marker='o', label=dijkstra[9][0])
plt.plot(dijkstra[14][4], dijkstra[14][1], 'm', marker='o', label=dijkstra[14][0])
plt.plot(dijkstra[19][4], dijkstra[19][1], 'g', marker='o', label=dijkstra[19][0])
plt.plot(dijkstra[24][4], dijkstra[24][1], 'r', marker='o', label=dijkstra[24][0])
plt.xlabel('Densità')
plt.ylabel('Tempo di esecuzione')
plt.title("Relazione Dijkstra: tempo di esecuzione, densità")
plt.legend()
plt.show()

plt.plot(dijkstra[24][3], dijkstra[24][1], 'r', marker='o', label=dijkstra[24][0])
plt.plot(dijkstra[4][3], dijkstra[4][1], 'b', marker='o', label=dijkstra[4][0])
plt.plot(dijkstra[9][3], dijkstra[9][1], 'y', marker='o', label=dijkstra[9][0])
plt.plot(dijkstra[14][3], dijkstra[14][1], 'm', marker='o', label=dijkstra[14][0])
plt.plot(dijkstra[19][3], dijkstra[19][1], 'g', marker='o', label=dijkstra[19][0])
plt.xlabel('Numero archi')
plt.ylabel('Tempo di esecuzione')
plt.title("Relazione Dijkstra: tempo di esecuzione, numero archi")
plt.legend()
plt.show()

plt.plot([dijkstra[0][2], dijkstra[1][2], dijkstra[2][2], dijkstra[3][2], dijkstra[4][2]], [dijkstra[0][1], dijkstra[1][1], dijkstra[2][1], dijkstra[3][1], dijkstra[4][1]], 'b', marker='o', label=(dijkstra[0][0])[:4])
plt.plot([dijkstra[5][2], dijkstra[6][2], dijkstra[7][2], dijkstra[8][2], dijkstra[9][2]], [dijkstra[5][1], dijkstra[6][1], dijkstra[7][1], dijkstra[8][1], dijkstra[9][1]], 'y', marker='o', label=(dijkstra[5][0])[:8])
plt.plot([dijkstra[10][2], dijkstra[11][2], dijkstra[12][2], dijkstra[13][2], dijkstra[14][2]], [dijkstra[10][1], dijkstra[11][1], dijkstra[12][1], dijkstra[13][1], dijkstra[14][1]], 'pink', marker='o', label=(dijkstra[10][0])[:8])
plt.plot([dijkstra[15][2], dijkstra[16][2], dijkstra[17][2], dijkstra[18][2], dijkstra[19][2]], [dijkstra[15][1], dijkstra[16][1], dijkstra[17][1], dijkstra[18][1], dijkstra[19][1]], 'lightblue', marker='o', label=(dijkstra[15][0])[:7])
plt.plot([dijkstra[20][2], dijkstra[21][2], dijkstra[22][2], dijkstra[23][2], dijkstra[24][2]], [dijkstra[20][1], dijkstra[21][1], dijkstra[22][1], dijkstra[23][1], dijkstra[24][1]], 'g--', marker='o', label=(dijkstra[20][0])[:6])
plt.plot([floyd[0][2], floyd[1][2], floyd[2][2], floyd[3][2], floyd[4][2]], [floyd[0][1], floyd[1][1], floyd[2][1], floyd[3][1], floyd[4][1]], 'r', marker='o', label=(dijkstra[0][0])[:4])
plt.plot([floyd[5][2], floyd[6][2], floyd[7][2], floyd[8][2], floyd[9][2]], [floyd[5][1], floyd[6][1], floyd[7][1], floyd[8][1], floyd[9][1]], 'r', marker='o', label=(dijkstra[5][0])[:8])
plt.plot([floyd[10][2], floyd[11][2], floyd[12][2], floyd[13][2], floyd[14][2]], [floyd[10][1], floyd[11][1], floyd[12][1], floyd[13][1], floyd[14][1]], 'r', marker='o', label=(dijkstra[10][0])[:8])
plt.plot([floyd[15][2], floyd[16][2], floyd[17][2], floyd[18][2], floyd[19][2]], [floyd[15][1], floyd[16][1], floyd[17][1], floyd[18][1], floyd[19][1]], 'r', marker='o', label=(dijkstra[15][0])[:7])
plt.plot([floyd[20][2], floyd[21][2], floyd[22][2], floyd[23][2], floyd[24][2]], [floyd[20][1], floyd[21][1], floyd[22][1], floyd[23][1], floyd[24][1]], 'r', marker='o', label=(dijkstra[20][0])[:6])
plt.xlabel('Numero nodi')
plt.ylabel('Tempo di esecuzione')
plt.title("Relazione Dijkstra - Floyd-Warshall")
plt.legend()
plt.show()
