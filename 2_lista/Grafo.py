import networkx as nx
import matplotlib.pyplot as plt

#Criação do grafo
G = nx.DiGraph()

# Adicionando os vertices

def mostrar_grafo():
  weight = nx.get_edge_attributes(G,'weight')
  pos =  nx.spring_layout(G)
  nx.draw(G,pos,with_labels=True)
  nx.draw_networkx_edge_labels(G.get_edge_data,pos,edge_labels=weight)
  plt.show()

for i in range(1,10):
  G.add_node(i)



# Adicionando arestas
G.add_edge(1, 2)

G.add_edge(1, 4)
G.add_edge(1, 5)
G.add_edge(1, 6)
G.add_edge(1, 7)

G.add_edge(2,3)
G.add_edge(2,4)

G.add_edge(3, 2)
G.add_edge(3, 4)

G.add_edge(4, 5)

G.add_edge(5, 6)

G.add_edge(7, 6)

G.add_edge(8, 1)
G.add_edge(8, 2)
G.add_edge(8, 7)

G.add_edge(9, 2)
G.add_edge(9, 8)
G.add_edge(9, 10)

G.add_edge(10, 2)
G.add_edge(10, 3)

print("Grafo sem os pesos:")
mostrar_grafo()

print()

MatrizIncidencia = nx.incidence_matrix(G)

print("Encontre a matriz incidente do grafo:")

print(MatrizIncidencia.todense())

MatrizAdjacente = nx.adjacency_matrix(G)

print()

print("Encontre a matriz adjacente do grafo:")

print(MatrizAdjacente.todense())

print()

print("Imprima a lista de vertices e arestas:")
print("Vertices: ", G.nodes())
print("Arestas: ", G.edges())

G.add_weighted_edges_from([(1, 5, 20), (1, 6, 5),(1,4,20),(1,2,10),(1,7,5)])
G.add_weighted_edges_from([(2,3,5),(2,4,10)])
G.add_weighted_edges_from([(3,2,15),(3,4,5)])
G.add_weighted_edges_from([(4,5,10)])
G.add_weighted_edges_from([(5,6,5)])
G.add_weighted_edges_from([(7,6,10)])
G.add_weighted_edges_from([(8,1,5),(8,2,20),(8,7,5)])
G.add_weighted_edges_from([(9,2,15),(9,10,10),(9,8,20)])
G.add_weighted_edges_from([(10,2,5),(10,3,15)])

print()

print("Pesos das arestas:")
MatrizPesos = nx.adjacency_matrix(G)

print(MatrizPesos.todense())

print()

print("Existe aresta nos seguintes pontos:")

def getAresta(u,v):
  if(G.has_edge(u,v)):
    print("pontos[",u,",",v,"]:",G.has_edge(u,v))


for j in range(1,11):
 for i in range(1,11):
  getAresta(i,j)


print()

print("Grafo com os pesos:")
mostrar_grafo()

print()

def eDirecionado(g):
  if nx.is_directed(G):
    print("O seu grafo é direcionado!")
  else:
    print("O seu grafo não é direcionado!")


eDirecionado(G)

print()

print("Imprimir pesos:")

def getWeight(u,v):
    if(G.has_edge(u,v)):
        print("pontos[",u,",",v,"]:",G.get_edge_data(u,v))

for j in range(1,11):
 for i in range(1,11):
  getWeight(i,j) 
