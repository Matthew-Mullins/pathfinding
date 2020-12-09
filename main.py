# git init      - Make directory a git repository

# git add .     - Add all files not staged
# git add main.py   - Stage specific files
# git add css   - Stage entire directory

# git commit -m "Message"   - Commit changes with a message

# git status    - Shows the current state of the repository

# git branch <branch_name>  - Create a new branch
# git branch -a     - List all remote or local branches
# git branch -d <branch_name>   - Delete a branch

# git checkout <branch_name>    - Start working on an existing branch
# git checkout -b <new_branch>  _ Create and start working in a new branch

# git merge <branch_name>   - Merge changes into current branch

# Remote repositories
# git remote <command> <remote_name> <remote_url>   - Add remote repository
# git remote -v     - List named remote repositories

# git clone <remote_url>    - Create local working copy of remote repository

# git pull <branch_name> <remote_url/remote_name>   - Get the latest version of a repository

# git push <remote_url/remote_name> <branch>    - Send local commits to the remote repository
# git push --all

import tkinter as tk
from tkinter import ttk

from algorithms import *

import time

class Tile:
    def __init__(self, frame, position):
        self.frame = frame
        self.position = position
        self.blocked = False

    def reset(self):
        self.set_block(False)
        self.set_start(False)
        self.set_end(False)

    def set_block(self, block=True):
        self.blocked = block
        if block:
            self.color = 'black'
        else:
            self.color = 'white'
        self.update_color()

    def set_start(self, start=True):
        if self.blocked:
            self.set_block(False)
        self.is_start = start
        if start:
            self.color = 'green'
        else:
            self.color = 'white'
        self.update_color()

    def set_end(self, end=True):
        if self.blocked:
            self.set_block(False)
        self.is_end = end
        if end:
            self.color = 'red'
        else:
            self.color = 'white'
        self.update_color()

    def update_color(self):
        self.frame.configure(bg=self.color)

class Application(tk.Frame):
    GRID_W = 50
    GRID_H = 50
    TILE_W = 16
    TILE_H = 16

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid = []
        self.reset()
        self.initialize()

    def reset(self):
        self.reset_body()
        self.running = False
        self.walls = set()
        self.start_tile = None
        self.end_tile = None

    def initialize(self):
        self.create_header()
        self.create_body()

    def create_header(self):
        frame_header = tk.Frame(self.master, bd=2, relief=tk.RAISED)
        frame_header.pack(side=tk.TOP, expand=tk.FALSE, fill=tk.X)

        label = tk.Label(frame_header, anchor=tk.W, text='Controls:')
        label.grid(row=0, column=0, sticky=tk.W)

        label = tk.Label(frame_header, anchor=tk.W, text='Left click to create the starting point.')
        label.grid(row=1, column=0, columnspan=2, sticky=tk.W)

        label = tk.Label(frame_header, anchor=tk.W, text='Right click to create the ending point.')
        label.grid(row=2, column=0, columnspan=2, sticky=tk.W)

        label = tk.Label(frame_header, anchor=tk.W, text='Hold Z and move the cursor to create walls.')
        label.grid(row=3, column=0, columnspan=2, sticky=tk.W)

        label = tk.Label(frame_header, anchor=tk.W, text='Hold X and move the cursor to remove walls.')
        label.grid(row=4, column=0, columnspan=2, sticky=tk.W)

        label = tk.Label(frame_header, anchor=tk.W, text='Pathfinding Algorithm:')
        label.grid(row=1, column=2, sticky=tk.W)

        algorithms = [
            'A*',
            'Dijkstra\'s',
            'Depth-First Search',
            'Breadth-First Search'
        ]
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set(algorithms[0])
        combobox = ttk.Combobox(frame_header, justify=tk.LEFT, textvariable=self.algorithm_var, values=algorithms, width=20)
        combobox.grid(row=1, column=3, sticky=tk.W)

        label = tk.Label(frame_header, anchor=tk.W, text='Pathfinding Delay (ms):')
        label.grid(row=2, column=2, sticky=tk.W)

        self.delay_var = tk.StringVar()
        self.delay_var.set(1000)
        entry_delay = tk.Entry(frame_header, justify=tk.RIGHT, textvariable=self.delay_var, width=5)
        entry_delay.grid(row=2, column=3, sticky=tk.W)

        button = tk.Button(frame_header, bg='green', text='Start', command=self.start)
        button.grid(row=3, column=2, columnspan=2, sticky=tk.NSEW)

        button = tk.Button(frame_header, bg='red', text='Reset', command=self.reset)
        button.grid(row=4, column=2, columnspan=2, sticky=tk.NSEW)

    def create_body(self):
        frame_body = tk.Frame(self.master, bd=2, relief=tk.RAISED)
        frame_body.pack(side=tk.TOP, expand=tk.FALSE, fill=tk.BOTH)
        for y in range(Application.GRID_H):
            row = []
            for x in range(Application.GRID_W):
                frame = tk.Frame(frame_body, bd=2, bg='white', height=Application.TILE_H, relief=tk.SUNKEN, width=Application.TILE_W)
                frame.grid(column=x, row=y, sticky=tk.NSEW)
                tile = Tile(frame, (x, y))

                frame.bind('<Button-1>', func=lambda e, tile=tile: self.set_start(tile))
                frame.bind('<Button-3>', func=lambda e, tile=tile: self.set_end(tile))
                row.append(tile)
            self.grid.append(row)

    def reset_body(self):
        if self.grid.count == 0:
            return
        for col in self.grid:
            for row in col:
                row.reset()

    def set_start(self, tile):
        if self.start_tile:
            self.start_tile.reset()
        self.start_tile = tile
        tile.set_start()

    def set_end(self, tile):
        if self.end_tile:
            self.end_tile.reset()
        self.end_tile = tile
        tile.set_end()

    def start(self):
        print(self.algorithm_var.get())

    def update(self):
        self.master.update()
        self.master.update_idletasks()

    def run(self):
        while True:
            if self.running:
                pass
            self.update()

def main():
    root = tk.Tk()
    root.title('Pathfinding Visualizer')
    root.resizable(width=tk.FALSE, height=tk.FALSE)
    root.withdraw()
    app = Application(root)
    root.deiconify()
    app.run()
    root.mainloop()

if __name__ == "__main__":
    main()