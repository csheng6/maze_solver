from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        if self._win is None:
            return
        self._x1 = top_left_x
        self._y1 = top_left_y
        self._x2 = bottom_right_x
        self._y2 = bottom_right_y
        if self.has_left_wall:
            line = Line(Point(top_left_x, top_left_y), Point(top_left_x, bottom_right_y))
            self._win.draw_line(line)
        else:
            line = Line(Point(top_left_x, top_left_y), Point(top_left_x, bottom_right_y))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(bottom_right_x, top_left_y), Point(bottom_right_x, bottom_right_y))
            self._win.draw_line(line)
        else:
            line = Line(Point(bottom_right_x, top_left_y), Point(bottom_right_x, bottom_right_y))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(top_left_x, top_left_y), Point(bottom_right_x, top_left_y))
            self._win.draw_line(line)
        else:
            line = Line(Point(top_left_x, top_left_y), Point(bottom_right_x, top_left_y))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(top_left_x, bottom_right_y), Point(bottom_right_x, bottom_right_y))
            self._win.draw_line(line)
        else:
            line = Line(Point(top_left_x, bottom_right_y), Point(bottom_right_x, bottom_right_y))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        start_x = ((self._x2 - self._x1) // 2 ) + self._x1
        start_y = ((self._y2 - self._y1) // 2 ) + self._y1
        end_x = ((to_cell._x2 - to_cell._x1) // 2 ) + to_cell._x1
        end_y = ((to_cell._y2 - to_cell._y1) // 2 ) + to_cell._y1
        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        if not undo:
            line_color = "red"
        else:
            line_color = "gray"
        self._win.draw_line(line, line_color)