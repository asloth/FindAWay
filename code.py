# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:53:18 2019

@author: Sara
"""

# Importando algunas librerías que utilizaremos

# Networkx para grafos
import networkx as nx
# Pandas
import pandas as pd
# Mathplotlib
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

cix = pd.read_csv('vertices.csv')

cix.set_index(["code"], inplace=True)
cix.head()

rutas_cix = pd.read_csv("rutascompletas.csv")
rutas_cix.head()

DG=nx.DiGraph()
for row in rutas_cix.iterrows():
    DG.add_edge(row[1]["origin"],
                row[1]["destination"],
                duration=row[1]["cost"])

DG.nodes(data=True)


#nx.draw_circular(DG, 
#                 node_color="lightblue",
#                edge_color="gray",
#                font_size=20,
#                 width=2, with_labels=True, node_size=3500,

#)











































def plot_shortest_path(path):
    print(path)
    positions = nx.circular_layout(DG)
    
    nx.draw(DG, pos=positions,
                node_color='lightblue',
                edge_color='gray',
                font_size=24,
                width=1, with_labels=True, node_size=3500, alpha=0.8
           )
    
    short_path=nx.DiGraph()
    for i in range(len(path)-1):
        short_path.add_edge(path[i], path[i+1])
    
    nx.draw(short_path, pos=positions,
                node_color='dodgerblue',
                edge_color='dodgerblue',
                font_size=24,
                width=3, with_labels=True, node_size=3000
           )
    plt.show()
    
    
    
#Algoritmo Dijstra con la libreria Networkx -Informada   
plot_shortest_path(nx.dijkstra_path(DG,'USAT','ENTRA',weight='cost'))

#Algoritmo A* con la libreria Networkx -Informada
#plot_shortest_path(nx.astar_path(DG, 'USAT', 'RIPLEY',weigth='cost'))