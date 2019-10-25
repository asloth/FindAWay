# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:55:43 2019

@author: Patrik
"""


import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import defaultdict, deque


plt.rcParams['figure.figsize'] = (20.0, 10.0)

cix = pd.read_csv('vertices.csv')

cix.set_index(["code"], inplace=True)
cix.head()

rutas_cix = pd.read_csv("rutascompletas.csv")
rutas_cix.head()

DG = nx.krackhardt_kite_graph()
for row in rutas_cix.iterrows():
    DG.add_edge(row[1]["origin"],
                row[1]["destination"],
                duration=row[1]["cost"])
DG.nodes(data=True)


print("Betweenness")
b = nx.betweenness_centrality(DG)
for v in DG.nodes():
    print("%0.2d %5.3f" % (v, b[v]))

print("Degree centrality")
d = nx.degree_centrality(DG)
for v in DG.nodes():
    print("%0.2d %5.3f" % (v, d[v]))

print("Closeness centrality")
c = nx.closeness_centrality(DG)
for v in DG.nodes():
   print("%0.2d %5.3f" % (v, c[v]))

nx.draw(DG)
plt.show()

def bfs_edges(G, source, reverse=False):
    """Produce edges in a breadth-first-search starting at source.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Specify starting node for breadth-first search and return edges in
       the component reachable from source.

    reverse : bool, optional
       If True traverse a directed graph in the reverse direction

    Returns
    -------
    edges: generator
       A generator of edges in the breadth-first-search.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([0,1,2])
    >>> print(list(nx.bfs_edges(G,0)))
    [(0, 1), (1, 2)]

    Notes
    -----
    Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    by D. Eppstein, July 2004.
    """
    if reverse and isinstance(G, nx.DiGraph):
        neighbors = G.predecessors_iter
    else:
        neighbors = G.neighbors_iter
    visited = set([source])
    queue = deque([(source, neighbors(source))])
    while queue:
        parent, children = queue[0]
        try:
            child = next(children)
            if child not in visited:
                yield parent, child
                visited.add(child)
                queue.append((child, neighbors(child)))
        except StopIteration:
            queue.popleft()

[docs]def bfs_tree(G, source, reverse=False):
    """Return an oriented tree constructed from of a breadth-first-search
    starting at source.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Specify starting node for breadth-first search and return edges in
       the component reachable from source.

    reverse : bool, optional
       If True traverse a directed graph in the reverse direction

    Returns
    -------
    T: NetworkX DiGraph
       An oriented tree

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([0,1,2])
    >>> print(list(nx.bfs_edges(G,0)))
    [(0, 1), (1, 2)]

    Notes
    -----
    Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    by D. Eppstein, July 2004.
    """
    T = nx.DiGraph()
    T.add_node(source)
    T.add_edges_from(bfs_edges(G,source,reverse=reverse))
    return T

[docs]def bfs_predecessors(G, source):
    """Return dictionary of predecessors in breadth-first-search from source.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Specify starting node for breadth-first search and return edges in
       the component reachable from source.

    Returns
    -------
    pred: dict
       A dictionary with nodes as keys and predecessor nodes as values.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([0,1,2])
    >>> print(nx.bfs_predecessors(G,0))
    {1: 0, 2: 1}

    Notes
    -----
    Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    by D. Eppstein, July 2004.
    """
    return dict((t,s) for s,t in bfs_edges(G,source))

[docs]def bfs_successors(G, source):
    """Return dictionary of successors in breadth-first-search from source.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Specify starting node for breadth-first search and return edges in
       the component reachable from source.

    Returns
    -------
    succ: dict
       A dictionary with nodes as keys and list of succssors nodes as values.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_path([0,1,2])
    >>> print(nx.bfs_successors(G,0))
    {0: [1], 1: [2]}

    Notes
    -----
    Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
    by D. Eppstein, July 2004.
    """
    d = defaultdict(list)
    for s,t in bfs_edges(G,source):
        d[s].append(t)
    return dict(d)



