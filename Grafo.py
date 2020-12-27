"""
Implementazione della classe grafo
Rappresentata attraverso le liste di adiacenza e matrice di adiacenza
"""

import sys
import pandas as pd


class GraphAdjList:
    """ Struttura del grafo realizzata mediante liste di adiacenza """

    def __init__(self, vertici, connections, directed=False):
        self.vertici = vertici
        self._directed = directed
        self.graph = {}
        self.init_adj(connections)
        # self.print_grafo()

    def init_adj(self, connections):
        """ Inizializzazione del grafo """
        for i in range(len(self.vertici)):
            self.graph[i] = []
        self.make_connections(connections)

    def make_connections(self, connections):
        for node1, node2, weight in connections:
            self.add(node1, node2, weight)

    def add(self, nodo1, nodo2, weight):
        """
        Aggiunge un arco tra i nodo1 e nodo2
        Se il grafo non è diretto, verifico precedentemente se esiste già una connessione tra tali nodi
        Pertanto, se il grafo è indiretto può esistere solo un arco u-v
        Se il grafo è diretto, possono esistere al massimo due archi, tali che u->v, v->u
        """
        if not self._directed:
            to_add = False
            if nodo2 not in (x[0] for x in self.graph[nodo1.name]) and nodo1 not in (x[0] for x in self.graph[nodo2.name]):
                to_add = True
            if to_add:
                self.graph[nodo1.name].append([nodo2, weight])
                self.graph[nodo2.name].append([nodo1, weight])
        else:
            if [nodo2, weight] not in self.graph[nodo1.name]:
                self.graph[nodo1.name].append([nodo2, weight])

    def print_grafo(self):
        """
        Stampa del grafo
        Per ogni vertice è presente la lista di adiacenza nella forma (nodo, peso)
        """
        for vertice in self.graph:
            adj_list = self.graph[vertice]
            print("Vertice " + str(vertice) + ":", end="")
            for i in range(0, len(adj_list)):
                print(" -> ({},".format(adj_list[i][0].name), "{})".format(adj_list[i][1]), end="")
            print(" \n")

    def get_archi(self, u):
        """ Ritorna la lista di adiacenza dell nodo u """
        adiacenza = self.graph[u.name]
        return adiacenza

    def get_nodo(self, n):
        """ Ritorna l'oggetto nodo richiesto """
        return self.vertici[n]


class GraphAdjMatrix:
    """ Struttura del grafo realizzata mediante matrice di adiacenza """

    def __init__(self, vertici, connections, directed):
        self.vertici = vertici
        self.graph = self.create_zero_matrix(len(vertici))
        self._directed = directed
        self.init(connections)

    @staticmethod
    def create_zero_matrix(n_vertici):
        mat = []
        for i in range(n_vertici):
            list = []
            for j in range(n_vertici):
                list.append(0)
            mat.append(list)
        return mat

    def init(self, connections):
        """ Inizializzazione del grafo """
        self.make_connections(connections)
        self.set_infinity()

    def set_infinity(self):
        """ Imposta a infinito la distanza tra i vertici che non sono connessi"""
        for riga in range(len(self.vertici)):
            for col in range(len(self.vertici)):
                if riga == col:
                    pass
                elif self.graph[riga][col] == 0:
                    self.graph[riga][col] = sys.maxsize

    def make_connections(self, connections):
        for node1, node2, weight in connections:
            self.add(node1, node2, weight)

    def add(self, nodo1, nodo2, weight):
        """
        Aggiunge un arco tra nodo1 e nodo2
        Se il grafo non è diretto, verifico precedentemente se posso aggiungere l'arco bidirezionale senza sovrascrivere
        precedenti valori
        Pertanto, se il grafo è indiretto può esistere solo un arco u-v
        Se il grafo è diretto, possono esistere al massimo due archi, tali che u->v, v->u
        """
        if not self._directed:
            to_add = False
            if self.graph[int(nodo1.name)][int(nodo2.name)] == 0 and self.graph[int(nodo2.name)][int(nodo1.name)] == 0:
                to_add = True
            if to_add:
                self.graph[int(nodo1.name)][int(nodo2.name)] = weight
                self.graph[int(nodo2.name)][int(nodo1.name)] = weight
        else:
            if self.graph[int(nodo1.name)][int(nodo2.name)] == 0:
                self.graph[int(nodo1.name)][int(nodo2.name)] = weight

    def print_grafo(self):
        """ Stampa del grafo """
        print("Stampa grafo:")
        n_elements = []
        for i in range(len(self.vertici)): n_elements.append(i)
        print_nice = pd.DataFrame(self.graph, index=n_elements, columns=n_elements)
        print(print_nice)

    def get_archi(self, u):
        """
        Ritorna la lista di adiacenza dell nodo u (riga della matrice)
        """
        adiacenza = self.graph[u.name]
        return adiacenza

    def get_nodo(self, n):
        """ Ritorna il nodo richiesto """
        return self.vertici[n]
