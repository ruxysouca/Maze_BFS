# Maze BFS Solver

A Python desktop application built with Tkinter that visualizes the shortest paths to all reachable exits in a grid-based maze. This project strictly implements Graph Theory principles by parsing a text matrix into a formal mathematical graph (nodes and adjacency list) before running the Breadth-First Search algorithm.

## Key Features
* **Formal Graph Architecture**: The grid is dynamically converted into vertices and edges (valid adjacent paths) to ensure optimal graph traversal.
* **Breadth-First Search**: Guarantees the discovery of the absolute shortest path to every accessible exit.
* **Interactive GUI**:
  * Custom start node selection via coordinate input fields.
  * Step-by-step path visualization using **Next** and **Prev** buttons to prevent visual overlap.
  * Valid paths are animated in **Green**.
  * Unreachable/blocked exits are highlighted in **Red**.
  * The selected starting point is marked in **Blue**.

## Maze Configuration
The maze is loaded from the `maze.txt` file. The encoding follows these rules:
* `1` represents a walkable path.
* `0` represents an impassable wall.
* Any `1` located on the outer boundaries of the grid is automatically recognized as an exit.

**Example `maze.txt`:**
```text
000001
111111
001000
101101
101101
