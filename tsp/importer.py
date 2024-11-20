import pandas as pd
import networkx as nx

def import_tsp_from_csv(file_path: str) -> nx.Graph:
    """
    Import a TSP instance from a CSV file containing a distance matrix
    and convert it to a NetworkX graph.
    
    Args:
        file_path: Path to the CSV file containing the distance matrix
        
    Returns:
        Tuple containing:
        - G: NetworkX graph with distances as edge weights
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
    
    # Add edges with weights
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes[i+1:], i+1):
            weight = df.iloc[i, j]
            # Verify symmetry
            if abs(weight - df.iloc[j, i]) > 1e-10:
                raise ValueError("Distance matrix must be symmetric")
            G.add_edge(node1, node2, weight=weight)
    
    return G
