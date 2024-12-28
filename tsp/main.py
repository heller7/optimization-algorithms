from importer import import_tsp_from_csv
from tsp_gurobi import solve_tsp

file_path = "tsp/data/example.csv"

G = import_tsp_from_csv(file_path)
tour, cost = solve_tsp(G)

print(f"Optimal tour: {' -> '.join(tour + [tour[0]])}")
print(f"Total distance: {cost}")