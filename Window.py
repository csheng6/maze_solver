from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title('Main Window')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width = self.width, height = self.height)
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=5)
        canvas.pack()

win = Window(800, 600)
point1 = Point(100,200)
point2 = Point(200,35)
line1 = Line(point1, point2)
win.draw_line(line1, "green")
win.wait_for_close()

""" win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300)
canvas.pack()

# Add a line in canvas widget
canvas.create_line(100,200,200,35, fill="green", width=5)

win.mainloop() """