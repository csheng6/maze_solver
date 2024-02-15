from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    maze = Maze(3, 3, 10, 10, 79, 79, win)
    maze.solve()
    win.wait_for_close()

main()