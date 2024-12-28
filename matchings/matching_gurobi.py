import gurobipy as gp
from gurobipy import GRB
import networkx as nx
from typing import List, Tuple

def solve_matching(G: nx.Graph) -> Tuple[List[str], float]:
    """
    Solve the matching problem using Gurobi.
    """
    try: 
        model = gp.Model('Matching')

        # Get nodes and number of nodes
        nodes = list(G.nodes())
        n = len(nodes)
        
        # Create binary variables for edges
        y = model.addVars([(i,j) for i, j in G.edges()], vtype=GRB.BINARY, name='y')

        # Objective: Maximize total matching
        model.setObjective(gp.quicksum(y[i,j] for i, j in y.keys()), GRB.MAXIMIZE)
        
        # Constraints for matching
        for i in nodes:
            # Sum over all edges incident to node i
            incident_edges = [(a,b) for (a,b) in G.edges() if a == i or b == i]
            model.addConstr(
                gp.quicksum(y[a,b] for (a,b) in incident_edges) <= 1, 
                f'match_{i}'
            )

        # Solve the model
        model.optimize()
        
        # Get the matching
        matching = [(i, j) for i, j in y.keys() if y[i,j].x == 1]
        return matching, model.objVal
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], 0.0
