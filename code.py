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

nx.draw_circular(DG, 
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=20,
                 width=2, with_labels=True, node_size=3500,
)
