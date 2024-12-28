from collections import deque

def bfs(G, start):
    """
    Perform breadth-first search on a NetworkX graph
    
    Args:
        G: NetworkX graph
        start: Starting node
    
    Returns:
        visited: Set of nodes visited in BFS order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

# Optional: If you want to get the BFS path/tree
def bfs_with_path(G, start):
    """
    Perform BFS and return parent dictionary for path reconstruction
    
    Args:
        G: NetworkX graph
        start: Starting node
    
    Returns:
        parent: Dictionary containing parent nodes for path reconstruction
    """
    parent = {start: None}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in G.neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    
    return parent

def get_all_bfs_paths(G, start):
    """
    Get all possible paths from start node to every other node using BFS
    
    Args:
        G: NetworkX graph
        start: Starting node
    
    Returns:
        paths: Dictionary with target nodes as keys and paths from start as values
    """
    parent = bfs_with_path(G, start)
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
