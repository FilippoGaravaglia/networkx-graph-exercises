import networkx as nx

def run():
    g = nx.Graph()
    g.add_edges_from([(1, 2), (2, 3), (3, 4)])
    print(g)