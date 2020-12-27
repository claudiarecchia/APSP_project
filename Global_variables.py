

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
p = 0.3
