from collections import defaultdict

 

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
