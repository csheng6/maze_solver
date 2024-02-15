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
            win=None,
            seed=None
            ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._adj_list = {}
        if seed:
            random.seed(seed)
        self._create_cells()
        self._build_adj_list()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited(0,0)
        self.solve()

    def _create_cells(self):
        for row in range(self.num_rows):
            _cell_rows = []
            for col in range(self.num_cols):
                _cell_rows.append(Cell(self._win))
            self._cells.append(_cell_rows)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(row, col)
        self._build_adj_list()

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

    def _break_walls_r(self, row_coord, col_coord):
        self._cells[row_coord][col_coord].visited = True
        copy_adj = self._adj_list[self._cells[row_coord][col_coord]]
        random.shuffle(copy_adj)
        for adjace in copy_adj:
            if not adjace['cell'].visited:
                self._break_walls_r(adjace['row'], adjace['col'])
                if adjace['neighbor'] == 'right':
                    self._cells[row_coord][col_coord].has_right_wall = False
                elif adjace['neighbor'] == 'bottom':
                    self._cells[row_coord][col_coord].has_bottom_wall = False
                elif adjace['neighbor'] == 'top':
                    self._cells[row_coord][col_coord].has_top_wall = False
                elif adjace['neighbor'] == 'left':
                    self._cells[row_coord][col_coord].has_left_wall = False
                self._draw_cell(row_coord, col_coord)

    def _build_adj_list(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                edges = []
                check_bottom_neighbor, check_left_neighbor, check_right_neighbor, check_top_neighbor = True, True, True, True
                for num_poss_edges in range(4):
                    try:
                        if check_bottom_neighbor:
                            edges.append({'cell': self._cells[row][col+1], 'row': row, 'col': col+1, 'neighbor': 'bottom'})
                            check_bottom_neighbor = False
                    except:
                        check_bottom_neighbor = False
                    try:
                        if check_right_neighbor:
                            edges.append({'cell': self._cells[row+1][col], 'row': row+1, 'col': col, 'neighbor':  'right'})
                            check_right_neighbor = False
                    except:
                     check_right_neighbor = False
                    try:
                        if check_top_neighbor and col-1 >= 0:
                            edges.append({'cell': self._cells[row][col-1], 'row': row, 'col': col-1, 'neighbor':  'top'})
                            check_top_neighbor = False
                        else:
                            check_top_neighbor = False
                    except:
                        check_top_neighbor = False
                    try:
                        if check_left_neighbor and row-1 >= 0:
                            edges.append({'cell': self._cells[row-1][col], 'row': row-1, 'col': col, 'neighbor':  'left'})
                            check_left_neighbor = False
                        else:
                            check_left_neighbor = False
                    except:
                        check_left_neighbor = False

                self._adj_list[self._cells[row][col]] = edges

    def _reset_cells_visited(self, row_coord, col_coord):
        if not self._cells[row_coord][col_coord].visited:
            return
        else:
            self._cells[row_coord][col_coord].visited = False
        for adjace in self._adj_list[self._cells[row_coord][col_coord]]:
            self._reset_cells_visited(adjace['row'], adjace['col'])

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, row_coord, col_coord):
        if self._cells[row_coord][col_coord].visited:
            return
        if row_coord == self.num_rows-1 and col_coord == self.num_cols-1:
            return True
        self._animate()
        self._cells[row_coord][col_coord].visited = True
        for adjace in self._adj_list[self._cells[row_coord][col_coord]]:
            if adjace['neighbor'] == 'right':
                if not self._cells[row_coord][col_coord].has_right_wall:
                    self._cells[row_coord][col_coord].draw_move(adjace['cell'])
                    if self._solve_r(adjace['row'], adjace['col']):
                        return True
                    else:
                        self._cells[row_coord][col_coord].draw_move(adjace['cell'], undo=True)
            elif adjace['neighbor'] == 'bottom':
                if not self._cells[row_coord][col_coord].has_bottom_wall:
                    self._cells[row_coord][col_coord].draw_move(adjace['cell'])
                    if self._solve_r(adjace['row'], adjace['col']):
                        return True
                    else:
                        self._cells[row_coord][col_coord].draw_move(adjace['cell'], undo=True)
            elif adjace['neighbor'] == 'left':
                if not self._cells[row_coord][col_coord].has_left_wall:
                    self._cells[row_coord][col_coord].draw_move(adjace['cell'])
                    if self._solve_r(adjace['row'], adjace['col']):
                        return True
                    else:
                        self._cells[row_coord][col_coord].draw_move(adjace['cell'], undo=True)
            elif adjace['neighbor'] == 'top':
                if not self._cells[row_coord][col_coord].has_top_wall:
                    self._cells[row_coord][col_coord].draw_move(adjace['cell'])
                    if self._solve_r(adjace['row'], adjace['col']):
                        return True
                    else:
                        self._cells[row_coord][col_coord].draw_move(adjace['cell'], undo=True)
        return False