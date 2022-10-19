import networkx as nx

grafo = nx.Graph()

# Adicionando os vertices
grafo.add_node(1)
grafo.add_node(2)
grafo.add_node(3)
grafo.add_node(4)
grafo.add_node(5)
grafo.add_node(6)
grafo.add_node(7)
grafo.add_node(8)
grafo.add_node(9)
grafo.add_node(10)

# Visualizando os vertices
print(grafo.nodes())

# Adicionando arestas

grafo.add_edge(1, 2)
grafo.add_edge(1, 4)
grafo.add_edge(1, 5)
grafo.add_edge(1, 6)
grafo.add_edge(1, 7)

grafo.add_edge(2, 3)
grafo.add_edge(2, 4)
grafo.add_edge(2, 4)

grafo.add_edge(3, 4)
grafo.add_edge(3, 2)

grafo.add_edge(4, 5)

grafo.add_edge(5, 6)

grafo.add_edge(7, 6)

grafo.add_edge(8, 1)
grafo.add_edge(8, 2)
grafo.add_edge(8, 7)

grafo.add_edge(9, 2)
grafo.add_edge(9, 10)
grafo.add_edge(9, 8)

grafo.add_edge(10, 2)
grafo.add_edge(10, 3)

# Imprimindo grafo

#nx.draw(grafo)

# Adicionando rotulos
#nx.draw(grafo, with_labels=True)

nx.draw(grafo, with_labels=True, node_size=1200, node_color='red',edge_color="tab:blue")
#B)
# Matrix adjacentes
matrixAd = nx.adjacency_matrix(grafo)
print(matrixAd.todense())

print()
#A)
#Matrix incidência
matrixAi = nx.incidence_matrix(grafo)
print(matrixAi.todense())

print()
#C)
#Arestas e vertices
print("Vertices: ", grafo.nodes())
print("Arestas: ", grafo.edges())

print()
#D)
