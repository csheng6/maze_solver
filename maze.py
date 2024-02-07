from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
            ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for row in range(self.num_rows):
            _cell_rows = []
            for col in range(self.num_cols):
                _cell_rows.append(Cell(self._win))
            self._cells.append(_cell_rows)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(row, col)

    def _draw_cell(self, row, col):
        if self._win is None:
            return
        top_left_x = self._x1 + row * self.cell_size_x
        top_left_y = self._y1 + col * self.cell_size_y
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y
        self._cells[row][col].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        rand_num = random.random()
        if rand_num < 0.5:
            self._cells[0][0].has_top_wall = False
        else:
            self._cells[0][0].has_left_wall = False
        rand_num = random.random()
        row = self.num_rows - 1
        col = self.num_cols - 1
        if rand_num < 0.5:
            self._cells[row][col].has_right_wall = False
        else:
            self._cells[row][col].has_bottom_wall = False
        self._draw_cell(0,0)
        self._draw_cell(row,col)