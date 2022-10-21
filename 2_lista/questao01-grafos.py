import networkx as nx
import matplotlib.pyplot as pyp

grafo = nx.DiGraph()

def exibir_grafo():
    weight = nx.get_edge_attributes(grafo,'weight')
    pos =  nx.spring_layout(grafo)
    nx.draw(grafo,pos,with_labels=True)
    nx.draw_networkx_edge_labels(grafo.get_edge_data,pos,edge_labels=weight)
    pyp.show()

for i in range(1,10):
    grafo.add_node(i)

grafo.add_edge(1,2)
grafo.add_edge(1,4)
grafo.add_edge(1,5)
grafo.add_edge(1,6)
grafo.add_edge(1,7)
grafo.add_edge(2,3)
grafo.add_edge(2,4)
grafo.add_edge(3,2)
grafo.add_edge(3,4)
grafo.add_edge(4,5)
grafo.add_edge(5,6)
grafo.add_edge(7,6)
grafo.add_edge(8,1)
grafo.add_edge(8,2)
grafo.add_edge(8,7)
grafo.add_edge(9,2)
grafo.add_edge(9,8)
grafo.add_edge(9,10)
grafo.add_edge(10,2)
grafo.add_edge(10,3)

print("f) Use o pacote Workx do Python, ou um pacote de outra linguagem para imprimir este grafo.")
exibir_grafo()
print()

incidencia = nx.incidence_matrix(grafo)

print("a) Encontre a matriz incidência do grafo.")

print(incidencia.todense())

adjacente = nx.adjacency_matrix(grafo)

print()

print("b) Encontre a matriz de adjacências do grafo.")

print(adjacente.todense())

print()

print("c) Imprima a lista de vertices e arestas do grafo.")
print("Vertices: ", grafo.nodes())
print("Arestas: ", grafo.edges())

grafo.add_weighted_edges_from([(1, 5, 20), (1, 6, 5),(1,4,20),(1,2,10),(1,7,5)])
grafo.add_weighted_edges_from([(2,3,5),(2,4,10)])
grafo.add_weighted_edges_from([(3,2,15),(3,4,5)])
grafo.add_weighted_edges_from([(4,5,10)])
grafo.add_weighted_edges_from([(5,6,5)])
grafo.add_weighted_edges_from([(7,6,10)])
grafo.add_weighted_edges_from([(8,1,5),(8,2,20),(8,7,5)])
grafo.add_weighted_edges_from([(9,2,15),(9,10,10),(9,8,20)])
grafo.add_weighted_edges_from([(10,2,5),(10,3,15)])

print()

print("d) Implemente um metodo para encontrar uma matriz de pesos de uma dada aresta.")
pesos = nx.adjacency_matrix(grafo)
print(pesos.todense())

print()

print("e) Use o metodo existe aresta para verificar se ha aresta dois vertices u e v.")
print()
print("Existe arestas nos pontos: ")

def getAresta(u,v):
    if(grafo.has_edge(u,v)):
        print("pontos[",u,",",v,"]:",grafo.has_edge(u,v))


for j in range(1,11):
    for i in range(1,11):
        getAresta(i,j)


print()

print("g) Na impressão do grafo coloque os pesos nas arestas correspondentes.")
exibir_grafo()

print()

print("h) Crie um metodo para saber se o grafo e direcionado ou nao.")
def eDirecionado(grafo):
    if nx.is_directed(grafo):
        print("Grafo direcionado.")
    else:
        print("Grafo nao direcionado.")

eDirecionado(grafo)

print()

print("i) Crie um metodo para imprimir o valor do peso entre dois vertices adjacentes.")

def getWeight(u,v):
    if(grafo.has_edge(u,v)):
        print("pontos[",u,",",v,"]:",grafo.get_edge_data(u,v))

for j in range(1,11):
    for i in range(1,11):
        getWeight(i,j) 