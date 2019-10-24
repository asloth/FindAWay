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

"""nx.draw(DG, 
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=20,
                 width=2, with_labels=True, node_size=3500,
)"""

#print (list(nx.all_shortest_paths(DG, source="METBAL", target="ENTRA", weight='cost')))
#print (list(nx.all_shortest_paths(DG, source="ENTRA", target="METBAL", weight='cost')))

def has_path(G, source, target):
    try:
        nx.shortest_path(G, source, target)
    except nx.NetworkXNoPath:
        return False
    return True

#print (has_path(DG,"METBAL", "ENTRA"))

def dfs_edges(G, source=None, depth_limit=None,target=None):
    if source is None:
        # edges for all components
        nodes = G
    else:
        # edges for components with source
        nodes = [source]
        final_target = [target]
        
    visited = set()
    if depth_limit is None:
        depth_limit = len(G)
        
    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, depth_limit, iter(G[start]))]
        while stack:
            parent, depth_now, children = stack[-1]
            try:
                child = next(children)
                
                if child not in visited:
                    yield parent, child
                    if child == final_target:
                        visited.add(child)
                    if depth_now > 1:
                        stack.append((child, depth_now - 1, iter(G[child])))
            except StopIteration:
                stack.pop()

print ( list(dfs_edges(DG,source="METBAL",depth_limit=None, target="PASEÑOPAZ")) )

"""

  
if child == final_target:
                    yield parent, child
                    visited.add(child)
                    depth_now=0
                    
                    
final_target = [target]
if child == final_target:
                    visited.add(child)
                    """