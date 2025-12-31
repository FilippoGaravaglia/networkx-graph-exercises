import networkx as nx

def degree_metric():
    g = nx.Graph()
    g.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 2)])

    node_degree_metric(g)

def node_degree_metric(graph):
    for node in graph.nodes():
        print(node, graph.degree(node))