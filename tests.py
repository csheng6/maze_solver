import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)
    
    def test_maze_create_cells_balanced(self):
        num_cols = 12
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_cells_big(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)
    
    def test_maze_create_cells_break_entrance_and_exit(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertIsNot(m1._cells[0][0].has_top_wall, m1._cells[0][0].has_left_wall)
        self.assertIsNot(m1._cells[(m1.num_rows)-1][(m1.num_cols)-1].has_right_wall, m1._cells[(m1.num_rows)-1][(m1.num_cols)-1].has_bottom_wall)
    
    def test_maze_break_walls_r(self):
        num_cols = 10
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        m1._break_walls_r(0,0)
        self.assertIsNot(m1._cells[0][0].has_bottom_wall, m1._cells[0][0].has_right_wall)

if __name__ == "__main__":
    unittest.main()