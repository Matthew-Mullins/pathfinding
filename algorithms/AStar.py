from algorithms import Algorithm

class AStar(Algorithm):
    def __init__(self, master, grid):
        Algorithm.__init__(self, master, grid)

    def heuristic(self):
        pass

    def run(self, start: tuple, goal: tuple):
        pass