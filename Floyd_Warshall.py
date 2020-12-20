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
                print("INF", end=" ")
            else:
                print(matrice[i][j], end="  ")
        print(" ")
