import tkinter as tk
from tkinter import messagebox
from collections import deque
from graph import MazeGraph

class MazeApp:

    def __init__(self, window):
        self.window = window
        self.window.title("Maze BFS Solver")

        self.maze = MazeGraph("maze.txt")
        self.cell_size = 100

        self.valid_paths = []
        self.unreachable_exits = []
        self.current_path_index = 0
        self.start_node = None

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

        self.prev_button = tk.Button(self.control_frame, text = "< Prev", command = self.show_prev, state = tk.DISABLED, font = ("Courier", 10, "bold"))
        self.prev_button.grid(row = 0, column = 5, padx = 5)

        self.path_label = tk.Label(self.control_frame, text = "Path: 0/0", font = ("Courier", 10, "bold"))
        self.path_label.grid(row = 0, column = 6, padx = 5)

        self.next_button = tk.Button(self.control_frame, text = "Next >", command = self.show_next, state = tk.DISABLED, font = ("Courier", 10, "bold"))
        self.next_button.grid(row = 0, column = 7, padx = 5)

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

        self.start_node = start_node
        self.run_bfs(start_node)

        if len(self.valid_paths) > 0:
            self.current_path_index = 0
            self.update_ui_for_paths()
            self.draw_current_path()
        else:
            self.path_label.config(text = "No paths!")
            self.draw_current_path()

    def run_bfs(self, start_node):
        queue = deque([start_node])
        visited = {start_node}
        parent = {start_node : None}

        while queue:
            current = queue.popleft()

            for neighbor in self.maze.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        self.valid_paths = []
        self.unreachable_exits = []

        for exit_node in self.maze.exits:
            if exit_node == start_node:
                continue

            if exit_node in visited:
                path = []
                step = exit_node
                while step != start_node:
                    path.append(step)
                    step = parent[step]
                path.reverse()
                self.valid_paths.append(path)
            else:
                self.unreachable_exits.append(exit_node)

    def update_ui_for_paths(self):
        total = len(self.valid_paths)
        current = self.current_path_index + 1
        self.path_label.config(text = f"Path: {current}/{total}")

        if self.current_path_index > 0:
            self.prev_button.config(state = tk.NORMAL)
        else:
            self.prev_button.config(state = tk.DISABLED)

        if self.current_path_index < total - 1:
            self.next_button.config(state = tk.NORMAL)
        else:
            self.next_button.config(state = tk.DISABLED)

    def show_prev(self):
        if self.current_path_index > 0:
            self.current_path_index -= 1
            self.update_ui_for_paths()
            self.draw_current_path()

    def show_next(self):
        if self.current_path_index < len(self.valid_paths) - 1:
            self.current_path_index += 1
            self.update_ui_for_paths()
            self.draw_current_path()

    def draw_current_path(self):
        self.draw_maze()

        for r, c in self.unreachable_exits:
            self.color_cell(r, c, "red")

        if self.valid_paths:
            current_path = self.valid_paths[self.current_path_index]
            for r, c in current_path:
                self.color_cell(r, c, "green")

        start_r, start_c = self.start_node
        self.color_cell(start_r, start_c, "blue")

    def color_cell(self, r, c, color):
        x1 = c * self.cell_size
        y1 = r * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = "gray")