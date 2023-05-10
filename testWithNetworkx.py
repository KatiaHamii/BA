import networkx as nx
import matplotlib.pyplot as plt

# Erstellen eines leeren Graphen
G = nx.DiGraph()

# Hinzufügen von Knoten
G.add_node('Erdbeben')
G.add_node('Tsunami')
G.add_node('Vulkan')
G.add_node('Hochwasser')

# Hinzufügen von Kanten mit Gewichtung
G.add_edge('Erdbeben', 'Tsunami', weight=0.5)
G.add_edge('Erdbeben', 'Vulkan', weight=0.3)
G.add_edge('Hochwasser', 'Tsunami', weight=0.2)

# Definieren der Positionen für die Knoten
pos = nx.spring_layout(G)

# Zeichnen des Graphen mit den Knoten und Kanten
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)

# Anzeigen des Graphen
plt.show()
