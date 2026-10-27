import tkinter as tk
from tkinter import messagebox
from graph import MazeGraph

class MazeApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Maze BFS Solver")

        self.maze = MazeGraph("maze.txt")
        self.cell_size = 100

        canvas_width = self.maze.cols * self.cell_size
        canvas_height = self.maze.rows * self.cell_size

        self.canvas = tk.Canvas(self.window, bg = "gray", width = canvas_width, height = canvas_height)
        self.canvas.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.control_frame = tk.Frame(self.window)
        self.control_frame.grid(row = 1, column = 0, pady = (0, 20))

        tk.Label(self.control_frame, text = "Starting row:", font = ("Courier", 10, "bold")).grid(row = 0, column = 0, padx = 5)
        self.row_entry = tk.Entry(self.control_frame, width = 5, font = ("Courier", 10, "italic"))
        self.row_entry.grid(row = 0, column = 1, padx = 5)

        tk.Label(self.control_frame, text = "Starting column:", font = ("Courier", 10, "bold")).grid(row = 0, column = 2, padx = 5)
        self.col_entry = tk.Entry(self.control_frame, width = 5, font = ("Courier", 10, "italic"))
        self.col_entry.grid(row = 0, column = 3, padx = 5)

        self.run_button = tk.Button(self.control_frame, text = "Run BFS", command = self.start_bfs, bg = "lightblue", font = ("Courier", 10, "bold"))
        self.run_button.grid(row = 0, column = 4, padx = 20)

        self.draw_maze()

    def draw_maze(self):
        for r in range(self.maze.rows):
            for c in range(self.maze.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if (r, c) in self.maze.nodes:
                    color = "white"
                else:
                    color = "black"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = "gray")

    def start_bfs(self):
        try:
            start_r = int(self.row_entry.get())
            start_c = int(self.col_entry.get())
        except ValueError:
            messagebox.showerror(title = "Error", message = "Please enter valid numbers for row and column!")
            return

        start_node = (start_r, start_c)
        if start_node not in self.maze.nodes:
            messagebox.showerror(title = "Error", message = "The start node must be on a white path (1), not a wall (0)!")
            return

        self.draw_maze()

        x1 = start_c * self.cell_size
        y1 = start_r * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill = "blue", outline = "gray")