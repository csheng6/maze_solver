from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    maze = Maze(3, 3, 10, 10, 79, 79, win)
    maze._break_entrance_and_exit()
    #point1 = Point(100,200)
    #point2 = Point(200,35)
    #line1 = Line(point1, point2)
    #cell1 = Cell(win)
    #cell1.draw(10, 10, 50, 50)
    #cell2 = Cell(win)
    #cell2.draw(50, 10, 90, 50)
    #cell1.draw_move(cell2)
    #win.draw_line(line1, "green")
    win.wait_for_close()

main()