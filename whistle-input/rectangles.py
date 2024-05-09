import pyglet

NUM_RECTANGLES = 10
SPACE = 10
RECTANGLE_HEIGHT_DIVIDER = 15

class Rectangles:

    def __init__(self, batch, window_height, window_width) -> None:
        self.window_height = window_height
        self.window_width = window_width
        self.batch = batch
        self.rectangles = []

    def generate_rectangles(self):
        rectangles = []
        rectangle_width = 40
        for index, rectangle in enumerate(range(NUM_RECTANGLES)):
            rectangle = pyglet.shapes.Rectangle(
                x=self.window_width / 2 - rectangle_width / 2,
                y=index * (self.window_height / 12 + SPACE),  # (/12 + SPACE) to leave space between the rectangles
                height=self.window_height / RECTANGLE_HEIGHT_DIVIDER,
                width=rectangle_width,
                color=(255, 255, 255),
                batch=self.batch
            )
            rectangles.append(rectangle)
        return rectangles
