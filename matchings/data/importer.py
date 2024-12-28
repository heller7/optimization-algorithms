import pandas as pd
import networkx as nx

def import_matching_from_csv(file_path: str) -> nx.Graph:
    """
    Import a matching instance from a CSV file containing an adjacency matrix
    and convert it to a NetworkX graph.
    
    Args:
        file_path: Path to the CSV file containing the adjacency matrix
        
    Returns:
        Tuple containing:
        - G: NetworkX graph
        - num_nodes: Number of nodes in the network
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=0, index_col=0, sep=';')
    
    # Get node labels
    nodes = df.index.tolist()
    
    # Create an empty undirected graph
    G = nx.Graph()
    
    # Add nodes
    G.add_nodes_from(nodes)
    
    # Add edges
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes[i+1:], i+1):
            if df.iloc[i, j] == 1 and node1 != node2 and df.iloc[j, i] == 1:
                G.add_edge(node1, node2)
    
    return G
