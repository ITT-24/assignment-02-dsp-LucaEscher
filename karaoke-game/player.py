from pyglet import shapes

class Player:

    def __init__(self, batch, window_height) -> None:
        self.width = 10
        self.height = 25
        self.window_height = window_height
        self.body = shapes.Rectangle(
            x=20,
            y= window_height / 2,
            width=self.width,
            height=self.height,
            color=(252, 173, 3),
            batch=batch
        )
        
    def update(self, freq):
        new_position = freq * 1.5
        print(f'freq = {new_position}')
        if new_position < self.window_height - self.body.height:
            self.body.y = new_position

    def draw(self):
        self.body.draw()
