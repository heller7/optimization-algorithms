def dfs(G, start):
    """
    Perform depth-first search on a NetworkX graph
    
    Args:
        G: NetworkX graph
        start: Starting node
    
    Returns:
        visited: Set of nodes visited in DFS order
    """
    visited = set()
    
    def dfs_recursive(node):
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs_recursive(neighbor)
                
    dfs_recursive(start)
    return visited

def dfs_with_path(G, start):
    """
    Perform DFS and return parent dictionary for path reconstruction
    
    Args:
        G: NetworkX graph
        start: Starting node
    
    Returns:
        parent: Dictionary containing parent nodes for path reconstruction
    """
    parent = {start: None}
    
    def dfs_recursive(node):
        for neighbor in G.neighbors(node):
            if neighbor not in parent:
                parent[neighbor] = node
                dfs_recursive(neighbor)
                
    dfs_recursive(start)
    return parent

def get_sequence_of_nodes(G, start):
    """
    Get the sequence of nodes from start node to every other node using DFS
    
    Args:
        G: NetworkX graph
        start: Starting node
    
    Returns:
        paths: Dictionary with target nodes as keys and paths from start as values
    """
    parent = dfs_with_path(G, start)
    paths = {}
    
    for node in G.nodes():
        if node == start:
            paths[node] = [start]
            continue
            
        if node not in parent:  # Node not reachable
            paths[node] = []
            continue
            
        # Reconstruct path from parent dictionary
        path = [node]
        current = node
        while parent[current] is not None:
            current = parent[current]
            path.append(current)
        paths[node] = list(reversed(path))
    
    return paths
