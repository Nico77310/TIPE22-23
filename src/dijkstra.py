import networkx as nx
import matplotlib.pyplot as plt
import random

# Modélisation d'une ville par un graphe.
# Les sommets sont les intersections et les arêtes sont les rues.
# Chaque rue a un poids qui représente la densité du trafic routier entre deux intersections par un entier arbitraire.
# L'objectif est de trouver le chemin le plus écologique entre deux intersections en évitant les rues les plus congestionnées.

# Algorithme de Dijkstra
def dijkstra(G, start, end):
    # Initialisation 
    dist = {v: float('inf') for v in G.nodes()}
    prev = {v: None for v in G.nodes()}
    dist[start] = 0
    Q = set(G.nodes())

    # Boucle principale
    while Q:
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)
        if dist[u] == float('inf'):
            break
        for v, weight in G[u].items():
            alt = dist[u] + weight['weight']
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    
    # Construction du chemin
    path = []
    u = end
    while prev[u]:
        path.append(u)
        u = prev[u]
    path.append(start)
    path.reverse()

    # Affichage du graphe
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    for i in range(len(path)-1):
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], width=5, edge_color='g')
    plt.show()

    return path, dist[end]

# Création d'un graphe 2D
G = nx.grid_2d_graph(4,4) # Choix d'une grille 4x4

# Ajout de poids aléatoires entre les entiers a et b sur les arêtes
def weight(G, a, b):
    for u, v, in G.edges(data=True):
        G[u][v]['weight'] = random.randint(a, b)
    return G

# Exemple d'utilisation
path, weight = dijkstra(weight(G, 1, 10), (0,0), (3,3))
print('Chemin :', path)
print('Poids total :', weight)