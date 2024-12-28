import networkx as nx

def import_random_graph(n: int, p: float) -> nx.Graph:
    return nx.gnp_random_graph(n, p)
