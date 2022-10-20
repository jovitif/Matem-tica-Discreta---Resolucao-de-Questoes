from collections import defaultdict
import networkx as nx
 

class Grafo(object):

    #Implementando básica de um grafo.

     # Inicializando  a estrutura básica de um grafo."""
    def __init__(self, arestas, direcionado=False):
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

 

    #Retorna a lista de vértices do grafo.

    def get_vertices(self):
        return list(self.adj.keys())

 

    #Retorna a lista de arestas do grafo.

    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

 

    #Adiciona arestas ao grafo.

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adiciona_arco(u, v)

 

 

    def adiciona_arco(self, u, v):
        #Adiciona uma aresta entre dois nós
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar aretas nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

 
    def adiciona_peso_em_aresta(self, v, a, p):
        self.adj[v][a]['peso'] = p

   #Existe uma aresta entre os vértices u e v?

    def existe_aresta(self, u, v):        
        return u in self.adj and v in self.adj[u]

 

 

   #Permite o acesso a estrutura de dados como o acesso a estruturas de dados padrão do Python

    def __len__(self):
        return len(self.adj)

 

   #Para que possamos imprimir o grafo de forma legível

    def __str__(self): 
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

 

   # Ao fazer grafo[v] obtenhamos a lista de adjacências do vértice v
    def __getitem__(self, v):
        return self.adj[v]


## Inicializando o grafo

arestas = [
    (1, 2), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 4),
    (3, 4), (3, 2), (4, 5), (5, 6), (7, 6), (8, 1), (8, 2),
    (8, 7), (9, 2), (9, 10), (9, 8), (10, 2), (10, 3)
]

grafo = Grafo(arestas, direcionado=True)
graf = nx.Graph()

# Adicionando os vertices
graf.add_node(1)
graf.add_node(2)
graf.add_node(3)
graf.add_node(4)
graf.add_node(5)
graf.add_node(6)
graf.add_node(7)
graf.add_node(8)
graf.add_node(9)
graf.add_node(10)

# Adicionando arestas

graf.add_edge(1, 2)
graf.add_edge(1, 4)
graf.add_edge(1, 5)
graf.add_edge(1, 6)
graf.add_edge(1, 7)

graf.add_edge(2, 3)
graf.add_edge(2, 4)

graf.add_edge(3, 4)
graf.add_edge(3, 2)

graf.add_edge(4, 5)

graf.add_edge(5, 6)

graf.add_edge(7, 6)

graf.add_edge(8, 1)
graf.add_edge(8, 2)
graf.add_edge(8, 7)

graf.add_edge(9, 2)
graf.add_edge(9, 10)
graf.add_edge(9, 8)

graf.add_edge(10, 2)
graf.add_edge(10, 3)

#A)
matrixAi = nx.incidence_matrix(graf)
print(matrixAi.todense())

#B)
# Matrix adjacentes
matrixAd = nx.adjacency_matrix(graf)
print(matrixAd.todense())

#C)
print("Vertices: ", graf.nodes())
print("Arestas: ", graf.edges())

#D)


#E)
grafo.existe_aresta(10, 2)

#F)
nx.draw(graf, with_labels=True, node_size=1200, node_color='red',edge_color="tab:blue")