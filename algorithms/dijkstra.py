from algorithms import Algorithm
import math
import time
class Dijkstra(Algorithm):
    def __init__(self, master, grid):
        Algorithm.__init__(self, master, grid)

    def run(self, start: tuple, goal: tuple):
        def get_min_dist():
            lowest = next(iter(open_set))
            for position in open_set:
                if dist[position] < dist[lowest]:
                    lowest = position
            return lowest

        def get_neighbours(current):
            neighbours = set()
            for y in range(current[1] - 1, current[1] + 2):
                if not 0 <= y < len(self.grid):
                    continue
                for x in range(current[0] - 1, current[0] + 2):
                    if not 0 <= x < len(self.grid[0]):
                        continue
                    if x == current[0] and y == current[1]:
                        continue
                    tile = self.grid[y][x]
                    if not tile.blocked:
                        neighbours.add((x, y))
            return neighbours

        def tile_dist(a, b):
            diff_x = abs(a[0] - b[0])
            diff_y = abs(a[1] - b[1])
            result = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
            return result

        open_set = set()
        dist = {}
        prev = {}
        for row in self.grid:
            for tile in row:
                dist[tile.position] = math.inf
                prev[tile.position] = None
                open_set.add(tile.position)
        dist[start] = 0

        while len(open_set) != 0:
            if not self.master.running:
                return
            current = get_min_dist()
            open_set.remove(current)
            if current == goal:
                return self.reconstruct_path(prev, current)
            tile = self.grid[current[1]][current[0]]
            if tile.position != start and tile.position != goal:
                tile.color = 'yellow'
                tile.update_color()
            for neighbour in get_neighbours(current):
                tmp_dist = dist[current] + tile_dist(current, neighbour)
                if tmp_dist < dist[neighbour]:
                    dist[neighbour] = tmp_dist
                    prev[neighbour] = current
                    tile = self.grid[neighbour[1]][neighbour[0]]
                    if tile.position != start and tile.position != goal:
                        tile.color = 'blue'
                        tile.update_color()
                time.sleep(float(self.master.delay_var.get()) / 1000.)
                self.master.update()
