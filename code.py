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

iata_spain = pd.read_csv('vertex.csv')

iata_spain.set_index(["code"], inplace=True)
iata_spain.head()

spain_flights = pd.read_csv("rutas.csv")
spain_flights.head()

DG=nx.DiGraph()
for row in spain_flights.iterrows():
    DG.add_edge(row[1]["origin"],
                row[1]["destination"],
                duration=row[1]["cost"])
    
DG.nodes(data=True)

nx.draw(DG, 
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=24,
                 width=2, with_labels=True, node_size=3500,
)
