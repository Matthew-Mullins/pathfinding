from algorithms import Algorithm
import math
import time
class AStar(Algorithm):
    def __init__(self, master, grid):
        Algorithm.__init__(self, master, grid)

    def lowest_f_score(self, open_set, f_score):
        lowest = next(iter(open_set))
        for position in open_set:
            if f_score[position] < f_score[lowest]:
                lowest = position
        return lowest

    def get_neighbours(self, current):
        neighbours = set()
        for y in range(current[1] - 1, current[1] + 2):
            if not 0 <= y < len(self.grid):
                continue
            for x in range(current[0] - 1, current[0] + 2):
                if not 0 <= x < len(self.grid[0]):
                    continue
                if current[0] == x and current[1] == y:
                    continue
                tile = self.grid[y][x]
                if not tile.blocked:
                    neighbours.add((x, y))
        return neighbours

    def d(self, current, neighbour):
        diff_x = abs(current[0] - neighbour[0])
        diff_y = abs(current[1] - neighbour[1])
        return math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))

    def run(self, start: tuple, goal: tuple):
        def heuristic(position):
            diff_x = abs(position[0] - goal[0])
            diff_y = abs(position[1] - goal[1])
            distance_to_goal = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
            return distance_to_goal

        open_set = set([start])
        
        came_from = {}

        g_score = {node.position: math.inf for row in self.grid for node in row}
        g_score[start] = 0

        f_score = {node.position: math.inf for row in self.grid for node in row}
        f_score[start] = heuristic(start)

        while len(open_set) != 0:
            if not self.master.running:
                return
            current = self.lowest_f_score(open_set, f_score)
            if current == goal:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            tile = self.grid[current[1]][current[0]]
            if tile.position != start and tile.position != goal:
                tile.color = 'yellow'
                tile.update_color()
            neighbours = self.get_neighbours(current)
            for neighbour in neighbours:
                ten_g_score = g_score[current] + self.d(current, neighbour)
                if ten_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = ten_g_score
                    f_score[neighbour] = g_score[neighbour] + heuristic(neighbour)
                    if neighbour not in open_set:
                        open_set.add(neighbour)
                        tile = self.grid[neighbour[1]][neighbour[0]]
                        if tile.position != start and tile.position != goal:
                            tile.color = 'blue'
                            tile.update_color()
            time.sleep(float(self.master.delay_var.get()) / 1000.)
            self.master.update()