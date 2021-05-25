import matplotlib.pyplot as plt
from IO_utilities import *


executions = get_values_from_results()

x_values = []
y_values = []
x_values_F = []
y_values_F = []
x_values_d_er01 = []
y_values_d_er01 = []
x_values_F_er01 = []
y_values_F_er01 = []

for ex in executions:
    if "BA" in ex[0]:
        if "D" in ex[1]:
            x_values.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            y_values.append(float(ex[3]))  # n_nodi
        elif "F" in ex[1]:
            x_values_F.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            y_values_F.append(float(ex[3]))  # n_nodi

    if "ER_p01" in ex[0]:
        if "D" in ex[1]:
            x_values_d_er01.append(float(ex[2]))  # tempo di esecuzione
            # y_values.append(float(ex[5]))  # indice di densità
            y_values_d_er01.append(float(ex[3]))  # n_nodi
        elif "F" in ex[1]:
            x_values_F_er01.append(float(ex[2]))  # tempo di esecuzione
            # y_values_F.append(float(ex[5]))  # indice di densità
            y_values_F_er01.append(float(ex[3]))  # n_nodi


plt.plot(x_values, y_values, 'b', label='Dijkstra')
plt.plot(x_values_F, y_values_F, 'r', label='Floyd-Warshall')
plt.title("Barabasi-Albert")
plt.xlabel('Tempo di esecuzione')
# plt.ylabel('Indice di densità')
plt.ylabel('Numero nodi')
plt.legend()
plt.show()

plt.plot(x_values_d_er01, y_values_d_er01, 'b', label='Dijkstra')
plt.plot(x_values_F_er01, y_values_F_er01, 'r', label='Floyd-Warshall')
plt.title("Erdős–Rényi, p=0.1")
plt.xlabel('Tempo di esecuzione')
plt.ylabel('Numero nodi')
plt.legend()
plt.show()


