import networkx as nx
from importer import import_random_graph
from bfs import bfs, bfs_with_path, get_all_bfs_paths
from dfs import dfs, get_sequence_of_nodes

# Create a sample graph
G = import_random_graph(10, 0.5)

# Run BFS
visited = bfs(G, start=0)
print(f"Visited nodes: {visited}")

# Get BFS paths
parent = bfs_with_path(G, start=0)
print(f"Parent dictionary: {parent}")

# Get all BFS paths
paths = get_all_bfs_paths(G, start=0)
print("All paths from start node:")
for target, path in paths.items():
    print(f"To node {target}: {path}")

    # Run DFS
visited = dfs(G, start=0)
print(f"Visited nodes: {visited}")

# Get DFS paths
paths = get_sequence_of_nodes(G, start=0)
print("\nAll paths from start node:")
for target, path in paths.items():
    print(f"To node {target}: {path}")


