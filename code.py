# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:53:18 2019

@author: Sara
"""

# Importando algunas librerías que utilizaremos

# Networkx para grafos
import networkx as nx 

from collections import defaultdict, deque

# Pandas
import pandas as pd
# Mathplotlib
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

cix = pd.read_csv('vertices.csv')

cix.set_index(["code"], inplace=True)

rutas_cix = pd.read_csv("rutacompleta.csv")

DG=nx.Graph()

for row in rutas_cix.iterrows():
    DG.add_edge(row[1]["origin"],
                row[1]["destination"],
                duration=row[1]["cost"])

DG.nodes(data=True)

def plot_shortest_path(path):
    print(path)
    positions = nx.circular_layout(DG)
    
    nx.draw(DG, pos=positions,
                node_color='lightblue',
                edge_color='gray',
                font_size=10,
                width=1, with_labels=True, node_size=1000, alpha=0.8
           )
    
    short_path=nx.DiGraph()
    for i in range(len(path)-1):
        short_path.add_edge(path[i], path[i+1])
    
    nx.draw(short_path, pos=positions,
                node_color='dodgerblue',
                edge_color='dodgerblue',
                font_size=10,
                width=3, with_labels=True, node_size=1000
           )
    plt.show()
    
    
    
#Algoritmo Dijstra con la libreria Networkx -Informada   
print('----------------------Dijkstra------------------')
plot_shortest_path(nx.dijkstra_path(DG,1,25,weight='cost'))

#Algoritmo A* con la libreria Networkx -Informada
print('-----------------------A*-----------------------')
plot_shortest_path(nx.astar_path(DG, 1, 25,weight='cost'))


print('--------------Shortest Path------------------')
print (list(nx.all_shortest_paths(DG, source=1, target=25, weight='cost')))
#print (list(nx.all_shortest_paths(DG, source="ENTRA", target="METBAL", weight='cost')))

def has_path(G, source, target):
    try:
        nx.shortest_path(G, source, target)
    except nx.NetworkXNoPath:
        return False
    return True

#print (has_path(DG,"10", "24"))

def dfs_edges(G, source=None, depth_limit=None,target=None):
    if source is None:
        # edges for all components
        nodes = G
    else:# edges for components with source
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
                        break
                    else:
                         visited.add(child)
                         if depth_now > 1:
                             stack.append((child, depth_now - 1, iter(G[child])))
            except StopIteration:
                stack.pop()
                
                
            
#Primero en Profundidad -No Informada
print('------------DFS--------------------')
print( list(dfs_edges(DG,source=1, target=25)) )

def bfs_edges(G,source=None,target=None):
    final_target = [target]
    neighbors = G.neighbors_iter
    visited = set([source])
    queue = deque([(source, neighbors(source))])
    while queue:
        parent, children = queue[0]
        try:
            child = next(children)
            if child not in visited:
                yield parent, child
                if child == final_target:
                    break
                else:
                    visited.add(child)
                    queue.append((child, neighbors(child)))
        except StopIteration:
            queue.popleft()

#print( list(bfs_edges(DG,source="METBAL",target="PASEÑOPAZ")))

"""

  
if child == final_target:
                    yield parent, child
                    visited.add(child)
                    depth_now=0
                    
                    
final_target = [target]
if child == final_target:
                    visited.add(child)
                    """

