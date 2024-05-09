from pyglet import shapes

START_POSITION = 20
PLAYER_SPEED = 1.5


class Player:

    def __init__(self, batch, window_height) -> None:
        self.width = 10
        self.height = 25
        self.window_height = window_height
        self.body = shapes.Rectangle(
            x=START_POSITION,
            y=window_height / 2,
            width=self.width,
            height=self.height,
            color=(252, 173, 3),
            batch=batch
        )

    def update(self, freq: float):
        new_position = freq * PLAYER_SPEED
        # print frequencie as input for player (can be removed if annoying) [[[nicht vergessen -> so gewollt]]]
        print(f'freq = {new_position}')
        if new_position < self.window_height - self.body.height:
            self.body.y = new_position

    def draw(self):
        self.body.draw()
