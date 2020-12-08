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

import time

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.initialize()

    def initialize(self):
        self.create_header()
        self.create_body()

    def create_header(self):
        pass

    def display_header(self):
        pass

    def create_body(self):
        pass

    def display_body(self):
        pass

    def run(self):
        pass

def main():
    root = tk.Tk()
    root.title('Pathfinding Visualizer')
    root.withdraw()
    app = Application(root)
    root.deiconify()
    app.run()

if __name__ == "__main__":
    pass