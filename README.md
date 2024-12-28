# optimization-algorithms

This repository contains implementations of various optimization algorithms for different Operations Research problems.

## Implementations

### TSP

The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits each node exactly once and returns to the origin node.

- **Exact Method**: Mixed Integer Programming implementation using Gurobi
  - Miller-Tucker-Zemlin (MTZ) formulation for subtour elimination
  - CSV-based instance import
  - NetworkX graph representation
- **Location**: `/tsp`

### Matching
A matching is a subset of the edge set of a graph where each node is incident to at most one edge of the chosen subset. A classic optimization problem is to find a maximum matching, i.e. a subset with as many edges as possible (not to be confused with a maximal matching!).

- **IP-Formulation**: Integer Programming implementation using Gurobi.
- **Location**: `/matching`

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Gurobi 10.0+
- NetworkX 3.1+
- Pandas 1.5+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/optimization-algorithms.git        
   ```
2. Install dependencies
3. Run the script

### Running the TSP Example

```bash
python tsp/main.py
```

## 📋 Planned Implementations

- [ ] Traveling Salesperson Problem (TSP)
- [ ] Set Covering Problem
- [ ] Maximum Flow Problem
- [ ] Matchings
- [ ] Vehicle Routing Problem (VRP)
- [ ] Facility Location Problem
- [ ] Knapsack Problem
- [ ] Bin Packing Problem

