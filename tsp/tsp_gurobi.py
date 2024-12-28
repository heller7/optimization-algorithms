import gurobipy as gp
from gurobipy import GRB
import networkx as nx
from typing import List, Tuple

def solve_tsp(G: nx.Graph) -> Tuple[List[str], float]:
    """
    Solve the TSP using Gurobi with MTZ formulation for subtour elimination.
    """
    try:
        model = gp.Model('TSP')
            
        # Get nodes and number of nodes
        nodes = list(G.nodes())
        n = len(nodes)
            
        # Create binary variables for edges
        x = model.addVars([(i, j) for i in nodes for j in nodes if i != j], vtype=GRB.BINARY, name='x')
            
        # Create continuous variables for MTZ formulation
        # u[i] represents the position of node i in the tour
        u = model.addVars(nodes, lb=0, ub=n-1, vtype=GRB.CONTINUOUS, name='u')
            
        # Objective: Minimize total distance
        model.setObjective(gp.quicksum(G[i][j]['weight'] * x[i,j] for i, j in x.keys()), GRB.MINIMIZE)
            
        # Constraints for entering nodes
        for j in nodes: model.addConstr(gp.quicksum(x[i,j] for i in nodes if i != j) == 1, f'enter_{j}')
            
        # Constraints for exiting nodes
        for i in nodes: model.addConstr(gp.quicksum(x[i,j] for j in nodes if i != j) == 1, f'exit_{i}')     
            
            # MTZ subtour elimination constraints
        # Fix the position of the first node
        model.addConstr(u[nodes[0]] == 0, "root")
            
        # Add MTZ constraints
        for i in nodes:
                for j in nodes[1:]:  # Skip first node as destination
                    if i != j:
                        model.addConstr(u[i] - u[j] + n * x[i,j] <= n - 1, f'mtz_{i}_{j}')
            
        # Optimize
        model.optimize()
            
        # Extract the solution
        if model.status == GRB.OPTIMAL:
                selected_edges = [(i, j) for i, j in x.keys() if x[i,j].X > 0.5]
                tour = get_tour_from_edges(selected_edges, nodes[0])
                optimal_cost = model.objVal
                return tour, optimal_cost
        else:
            raise ValueError("No optimal solution found")
                
    except gp.GurobiError as e:
        print(f"Gurobi Error: {e}")
        raise
    finally:
        if 'model' in locals():
            model.dispose()

def get_tour_from_edges(edges: List[Tuple[str, str]], start_node: str) -> List[str]:
    """
    Convert a list of edges into an ordered tour.
    """
    adj = {node: [] for node in {v for edge in edges for v in edge}}
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    
    tour = [start_node]
    current = start_node
    
    while len(tour) < len(adj):
        next_node = [n for n in adj[current] if n not in tour][0]
        tour.append(next_node)
        current = next_node
    
    return tour

