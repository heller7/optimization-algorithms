from matching_gurobi import solve_matching
from matchings.importer import import_matching_from_csv

file_path = "matchings/data/graph.csv"

G = import_matching_from_csv(file_path)
matching, edge_count = solve_matching(G)

print(f"Maximum matching: {matching}")
print(f"Number of edges: {edge_count}")