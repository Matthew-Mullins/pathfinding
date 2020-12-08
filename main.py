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

import time

class Application(tk.Frame):
    GRID_W = 50
    GRID_H = 50
    TILE_W = 16
    TILE_H = 16

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.reset()
        self.initialize()

    def reset(self):
        self.running = False

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

    def create_body(self):
        self.grid = []
        frame_body = tk.Frame(self.master, bd=2, relief=tk.RAISED)
        frame_body.pack(side=tk.TOP, expand=tk.FALSE, fill=tk.BOTH)
        for y in range(Application.GRID_H):
            row = []
            for x in range(Application.GRID_W):
                frame = tk.Frame(frame_body, bd=2, height=Application.TILE_H, relief=tk.SUNKEN, width=Application.TILE_W)
                frame.grid(column=x, row=y, sticky=tk.NSEW)
                frame.bind('<Button-1>', func=lambda e: self.set_start(e))
                frame.bind('<Button-3>', func=lambda e: self.set_end(e))

    def set_start(self, e):
        print(e.widget)

    def set_end(self, e):
        print(e.widget)

    def reset_body(self):
        pass

    def update_speed(self):
        pass

    def start(self):
        pass

    def run(self):
        while True:
            if self.running:
                pass
            self.master.update()
            self.master.update_idletasks()

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