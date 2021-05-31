
from main import *

if __name__ == '__main__':
    graph_list = []
    real_graph_list = []
    for folder in folders:
        for filename in os.listdir("./" + folder):
            file_name = filename.replace('.csv', '')
            if folder == folders[0]:
                graph_list.append(file_name)
            else:
                real_graph_list.append(file_name)

    graph_list = sorted(graph_list)

    list1 = graph_list[0:5]
    list2 = graph_list[5:10]
    list3 = graph_list[10:15]
    list4 = graph_list[15:20]
    list5 = graph_list[20:25]
    g_list = []

    list_input = int(input("1 to 6: "))

    if list_input == 1: g_list = list1
    if list_input == 2: g_list = list2
    if list_input == 3: g_list = list3
    if list_input == 4: g_list = list4
    if list_input == 5: g_list = list5
    if list_input == 6: g_list = real_graph_list

    for file_name in g_list:
        print(file_name)
        connections, vertici = create_connections_from_file(file_name)

        # execute_with_networkit(file_name)
        if DIR:
            index = len(connections) / (len(vertici) * (len(vertici) - 1))  # L / n(n - 1)
        else:
            index = (2 * (len(connections))) / (len(vertici) * (len(vertici) - 1))  # 2L / n(n - 1)

        time, mat_f = execute_FloydWarshall(vertici, connections)
        report_exec_time(file_name, "F", time, len(vertici), len(connections), index)

        time = execute_Dijkstra_APSP(vertici, connections)
        report_exec_time(file_name, "D", time, len(vertici), len(connections), index)

        time = execute_Dijkstra_APSP_parallel(vertici, connections)
        report_exec_time(file_name, "DP", time, len(vertici), len(connections), index)