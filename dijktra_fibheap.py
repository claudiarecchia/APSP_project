import fibonacci_heap
import sys
import fibheap

class Vertice:
    def __init__(self, nodo):
        self.id = nodo
        self.adiacenza = {}
        # Imposto la distanza a infinito per tutti i nodi
        self.distanza = sys.maxsize  # o float("inf")
        # Imposto il nodo come non visitato
        self.visitato = False
        # Predecessore
        self.predecessore = None

    def aggiungi_vicino(self, vicino, peso=0):
        self.adiacenza[vicino] = peso

    def get_connessioni(self):
        return self.adiacenza.keys()

    def get_id(self):
        return self.id

    def get_peso(self, vicino):
        return self.adiacenza[vicino]

    def set_distanza(self, dist):
        self.distanza = dist

    def get_distanza(self):
        return self.distanza

    def set_predecessore(self, pred):
        self.predecessore = pred

    def set_visitato(self):
        self.visitato = True


class Graph:
    def __init__(self):
        self.dizionario_vertici = {}
        self.num_vertici = 0

    def __iter__(self):
        return iter(self.dizionario_vertici.values())

    def add_vertice(self, nodo):
        self.num_vertici = self.num_vertici + 1
        nuovo_vertice = Vertice(nodo)
        self.dizionario_vertici[nodo] = nuovo_vertice
        return nuovo_vertice

    def get_vertice(self, n):
        if n in self.dizionario_vertici:
            return self.dizionario_vertici[n]
        else:
            return None

    def add_arco(self, nodo_partenza, nodo_arrivo, peso=0):
        if nodo_partenza not in self.dizionario_vertici:
            self.add_vertice(nodo_partenza)
        if nodo_arrivo not in self.dizionario_vertici:
            self.add_vertice(nodo_arrivo)

        self.dizionario_vertici[nodo_partenza].aggiungi_vicino(self.dizionario_vertici[nodo_arrivo], peso)
        self.dizionario_vertici[nodo_arrivo].aggiungi_vicino(self.dizionario_vertici[nodo_partenza], peso)

    def get_vertici(self):
        return self.dizionario_vertici.keys()

    def set_predecessore(self, corrente):
        self.predecessore = corrente


def shortest(nodo, cammino):
    ''' costruzione del cammino minimo da nodo.predecessore'''
    if nodo.predecessore:
        cammino.append(nodo.predecessore.get_id())
        shortest(nodo.predecessore, cammino)
    return


def dijkstra(grafo, nodo_partenza):
    '''Dijkstra's shortest path'''
    # Imposto la distanza del nodo di partenza a zero
    nodo_partenza.set_distanza(0)

    da_visitare = [(v.get_distanza(), v) for v in grafo]
    fheap = fibonacci_heap.FibonacciHeap()
    for vertice in da_visitare:
        fheap.insert_node(vertice)

    while len(da_visitare):
        # print("lista di nodi da visitare:")
        # print(da_visitare)

        # Rimuovo un vertice con la distanza minore
        arco_uv = fheap.extract_min()
        nodo_corrente = arco_uv[1]
        nodo_corrente.set_visitato()

        # elimino il nodo visitato dalla lista
        for nodo in da_visitare:
            if nodo[1] == nodo_corrente:
                da_visitare.remove(nodo)

        # per i prossimi vertici adiacenti
        for prossimo_nodo in nodo_corrente.adiacenza:
            # se è stato visitato, vado avanti
            if prossimo_nodo.visitato:
                continue
            nuova_distanza = nodo_corrente.get_distanza() + nodo_corrente.get_peso(prossimo_nodo)

            if nuova_distanza < prossimo_nodo.get_distanza():
                prossimo_nodo.set_distanza(nuova_distanza)
                prossimo_nodo.set_predecessore(nodo_corrente)
                print('Aggiornato => corrente = %s; prossimo = %s; nuova distanza = %s;' % (nodo_corrente.get_id(), prossimo_nodo.get_id(), prossimo_nodo.get_distanza()))
            else:
                print('Non aggiornato => corrente = %s; next = %s; nuova distanza = %s;' % (nodo_corrente.get_id(), prossimo_nodo.get_id(), prossimo_nodo.get_distanza()))

        # Ricostruzione dello heap con i nuovi valori

        # Tolgo tutti gli elementi
        for i in range(len(da_visitare)):
            fheap.extract_min()

        # Inserisco tutti i vertici non visitati nella coda con priorità fheap
        da_visitare = [(v.get_distanza(), v) for v in grafo if not v.visitato]
        for vertice in da_visitare:
            fheap.insert_node(vertice)


if __name__ == '__main__':

    g = Graph()

    g.add_vertice('a')
    g.add_vertice('b')
    g.add_vertice('c')
    g.add_vertice('d')
    g.add_vertice('e')
    g.add_vertice('f')

    g.add_arco('a', 'b', 7)
    g.add_arco('a', 'c', 9)
    g.add_arco('a', 'f', 14)
    g.add_arco('b', 'c', 10)
    g.add_arco('b', 'd', 15)
    g.add_arco('c', 'd', 11)
    g.add_arco('c', 'f', 2)
    g.add_arco('d', 'e', 6)
    g.add_arco('e', 'f', 9)

    # print('Graph data:')
    # for v in g:
    #     for w in v.get_connessioni():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print('( %s , %s, %3d)' % (vid, wid, v.get_peso(w)))


dijkstra(g, g.get_vertice('a'))

target = g.get_vertice('e')
path = [target.get_id()]
shortest(target, path)
print('Cammino minimo: %s' % (path[::-1]))

