import tkinter as tk
from graph import MazeGraph

class MazeApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Maze BFS Solver")
        self.window.geometry("800x600")

        self.maze = MazeGraph("maze.txt")

        self.canvas = tk.Canvas(self.window, bg = "gray", width = 600, height = 500)
        self.canvas.grid(row = 0, column = 0, padx = 100, pady = 50)
