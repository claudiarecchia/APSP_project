"""
Implementazione dell'algoritmo APSP di Floyd-Warshall
Algoritmo per grafi orientati o non orientati
"""

import sys
from FibHeap import *
from Grafo import GraphAdjMatrix
from random import *
import time
from IO_utilities import *
import pandas as pd


def floyd_warshall(grafo):
    vertici = grafo.vertici
    matrice = grafo.graph
    for k in range(len(vertici)):
        for i in range(len(vertici)):
            for j in range(len(vertici)):
                matrice[i][j] = min(matrice[i][j], matrice[i][k] + matrice[k][j])
    print_solution(matrice, vertici)


def print_solution(matrice, vertici):
    for i in range(len(vertici)):
        for j in range(len(vertici)):
            if matrice[i][j] == sys.maxsize:
                matrice[i][j] = "INF"
    n_elements = []
    for i in range(len(vertici)): n_elements.append(i)
    print_nice = pd.DataFrame(matrice, index=n_elements, columns=n_elements)
    print(print_nice)
