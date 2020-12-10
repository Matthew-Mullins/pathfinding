import tkinter as tk
import time
class Algorithm:
    def __init__(self, master, grid):
        self.master = master
        self.grid = grid

    # Override this for each
    def run(self):
        pass

    def reconstruct_path(self, came_from: dict, current):
        sleep_time = float(self.master.delay_var.get()) / 1000.
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current)
            tile = self.master.grid[current[1]][current[0]]
            if tile != self.master.start_tile and tile != self.master.end_tile:
                tile.color = 'purple'
                tile.update_color()
            else:
                continue
            time.sleep(sleep_time)
            self.master.update()
        return total_path