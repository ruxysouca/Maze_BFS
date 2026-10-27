class MazeGraph:

    def __init__(self, filename):
      self.filename = filename
      self.nodes = set()

      self.adjacency_list = {}

      self.exits = []

      self.rows = 0
      self.cols = 0

      self.load_from_file()
      self.build_graph()
      self.find_exits()

    def load_from_file(self):
        with open(self.filename, 'r') as f:
            lines = f.read().splitlines()

        self.rows = len(lines)
        self.cols = len(lines[0]) if self.rows > 0 else 0

        for r in range(self.rows):
            for c in range(self.cols):
                if lines[r][c] =='1':
                    self.nodes.add((r, c))

    def build_graph(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for node in self.nodes:
            r, c = node

            self.adjacency_list[node] = []

            for dr, dc in directions:
                neighbor = (r + dr, c + dc)
                if neighbor in self.nodes:
                    self.adjacency_list[node].append(neighbor)

    def find_exits(self):
        for r, c in self.nodes:
            if r == 0 or r == self.rows - 1 or c == 0 or c == self.cols -1:
                self.exits.append((r, c))