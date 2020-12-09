import tkinter as tk

class Algorithm:
    def __init__(self, master, grid):
        self.master = master
        self.grid = grid

    def reconstruct_path(self, came_from: dict, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current)
        return total_path