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
        # self.print_graph()

    def init_adj(self, connections):
        """ Inizializzazione del grafo """
        for vertice in self.vertici:
        # for i in range(int(vertici[len(vertici)-1].name)):
            # self.graph[i] = []
            self.graph[vertice] = []
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
            if nodo2 not in (x[0] for x in self.graph[nodo1]) and nodo1 not in (x[0] for x in self.graph[nodo2]):
                to_add = True
            if to_add:
                self.graph[nodo1].append([nodo2, weight])
                self.graph[nodo2].append([nodo1, weight])
        else:
            # se è già stato inserito un arco da nodo1->nodo2, non verrà più modificato con eventuali altri valori
            if nodo2 not in (x[0] for x in self.graph[nodo1]):
                self.graph[nodo1].append([nodo2, weight])

    def print_graph(self):
        """
        Stampa del grafo
        Per ogni vertice è presente la lista di adiacenza nella forma (nodo, peso)
        """
        for vertice in self.graph:
            adj_list = self.graph[vertice]
            print("Vertice " + str(vertice.name) + ":", end="")
            for i in range(0, len(adj_list)):
                print(" -> ({},".format(adj_list[i][0].name), "{})".format(adj_list[i][1]), end="")
            print(" \n")

    def get_edges(self, u):
        """ Ritorna la lista di adiacenza dell nodo u """
        # adiacenza = self.graph[u.name]
        adiacenza = self.graph[u]
        return adiacenza

    def get_node(self, n):
        """ Ritorna l'oggetto nodo richiesto """
        return self.vertici[n]


class GraphAdjMatrix:
    """ Struttura del grafo realizzata mediante matrice di adiacenza """

    def __init__(self, vertici, connections, directed):
        self.vertici = vertici
        self.graph = self.create_zero_matrix(len(vertici))
        self._directed = directed
        self.init(connections)
        # self.print_graph()

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
            if self.graph[nodo1.index][nodo2.index] == 0:
                self.graph[nodo1.index][nodo2.index] = weight

    def print_graph(self):
        """ Stampa del grafo """
        print("Stampa grafo:")
        n_elements = []
        for vertex in self.vertici: n_elements.append(vertex.name)
        print_nice = pd.DataFrame(self.graph, index=n_elements, columns=n_elements)
        print(print_nice)

    def get_edges(self, u):
        """
        Ritorna la lista di adiacenza dell nodo u (riga della matrice)
        """
        adiacenza = self.graph[u.index]
        return adiacenza

    def get_node(self, n):
        """ Ritorna il nodo richiesto """
        return self.vertici[n]
