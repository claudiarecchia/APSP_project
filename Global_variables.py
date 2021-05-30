

# valore massimo assegnato al peso di ciascun arco creato
MAX = 50

# grafo diretto o indiretto
DIR = True

# per migliorare la qualità della generazione di valori random, vengono utilizzate le convenzioni:
# - tempo di sistema per l'inizializzazione del seed poichè difficile da replicare (file IO_utilities.py)
# - Teorema di Hull-Dobell, cioè
#   - a,m coprimi
#   - a-1 divisibile per tutti i fattori primi di m
#   - a-1 multiplo di 4 se m è multiplo di 4

m = 2 ** 32
b = 12345
a = 1103515245

# probabilità per la creazione di archi nel'algoritmo Erdős–Rényi
p = 0.1

# Number of attachments per node - usato nella costruzione dei grafi mediante Barabasi-Albert
k = 2

# cartella di destinazione grafi generati
graph_dir = "generated_graphs"

# cartella reperimento grafi reali
real_graph_dir = "grafi_reali_csv"

# cartella reperimento dati sulle esecuzioni degli algoritmi
report_dir = "results"

# nome file utilizzato per reperire i dati delle esecuzioni degli algoritmi
report_file = "results"

folders = [graph_dir, real_graph_dir]

# variabile per controllare i risultati ottenuti dagli esperimenti Floyd-Warshall, Dijkstra, NetworKit,
# mediante l'utilizzo dell'assert
check = False