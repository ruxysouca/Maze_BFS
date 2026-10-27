# Maze BFS Solver

A Python desktop application built with Tkinter that visualizes the shortest paths to all reachable exits in a grid-based maze. This project strictly implements Graph Theory principles by parsing a text matrix into a formal mathematical graph (nodes and adjacency list) before running the Breadth-First Search algorithm.

## Project Goal
This project was developed to demonstrate the practical application of Graph Theory. The primary objective is to strictly avoid parsing the labyrinth as a standard 2D matrix. Instead, the grid is formally converted into a mathematical graph (adjacency list), which is then traversed using the BFS algorithm to determine the shortest optimal paths to multiple exits.

## Key Features
* **Formal Graph Architecture**: The grid is dynamically converted into vertices and edges (valid adjacent paths) to ensure optimal graph traversal.
* **Breadth-First Search**: Guarantees the discovery of the absolute shortest path to every accessible exit.
* **Interactive GUI**:
  * Custom start node selection via coordinate input fields.
  * Step-by-step path visualization using **Next** and **Prev** buttons to prevent visual overlap.
  * Valid paths are animated in **Green**.
  * Unreachable/blocked exits are highlighted in **Red**.
  * The selected starting point is marked in **Blue**.

## Project Structure
The codebase follows a modular architecture to separate mathematical logic from the graphical interface:
- `graph.py`: The mathematical engine. It parses the input file, identifies vertices (`1`), and builds the adjacency list.
- `maze_app.py`: The GUI and algorithmic core. It manages the Tkinter canvas, handles user input, executes the BFS algorithm, and animates the paths.
- `main.py`: The entry point that initializes and launches the application.

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
