import tkinter as tk
from tkinter import messagebox  
from collections import deque
import random
import time

class MazeSolverGUI:
    def __init__(self, master, maze_size):
        self.master = master
        self.master.title("Maze Navigator")

        self.maze_size = maze_size
        self.maze = [[0] * maze_size for _ in range(maze_size)]
        self.generate_maze()

        self.canvas = tk.Canvas(self.master, width=maze_size*20, height=maze_size*20, bg='white')
        self.canvas.pack()

        self.draw_maze()

        self.start = (0, 0)
        self.end = (maze_size-1, maze_size-1)
        self.shortest_path = self.find_shortest_path()

        self.solve()

    def generate_maze(self):
        for i in range(self.maze_size):
            if i % 2 == 1:
                self.maze[i][random.randint(0, self.maze_size-1)] = 1

    def draw_maze(self):
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill='black')

    def find_shortest_path(self):
        visited = set()
        queue = deque([(self.start, [])])

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == self.end:
                return path + [(x, y)]

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.maze_size and 0 <= new_y < self.maze_size and self.maze[new_x][new_y] != 1 and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append(((new_x, new_y), path + [(x, y)]))

    def solve(self):
        for idx, (i, j) in enumerate(self.shortest_path):
            color = '#%02x%02x%02x' % (255, 0, int(255 * (1 - idx / len(self.shortest_path))))
            self.canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=color)
            self.master.update()
            time.sleep(0.1)

      
        messagebox.showinfo("Destination Reached", "Congratulations! You reached the destination.")

def main():
    maze_size = 20
    root = tk.Tk()
    app = MazeSolverGUI(root, maze_size)
    root.mainloop()

if __name__ == "__main__":
    main()
