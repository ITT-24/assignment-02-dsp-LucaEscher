from config import CHUNK_SIZE, CHANNELS, RATE, FORMAT, set_up_stream
from game import Game
import numpy as np
import os
import pyglet

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
stream = set_up_stream(FORMAT, CHANNELS, RATE, CHUNK_SIZE)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        os._exit(0)
    if symbol == pyglet.window.key.SPACE:
        global game
        game.game_state = 1

@window.event
def on_draw():
    window.clear()
    #aus audio-sample.py kopiert -----------
    data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
    # Convert audio data to numpy array
    data = np.frombuffer(data, dtype=np.int16)
    # -------------------------------------

    game.update(data)
    game.draw()


if __name__ == '__main__':
    global game
    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)
    game.run()
