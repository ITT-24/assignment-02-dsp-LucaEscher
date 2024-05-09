from config import CHUNK_SIZE, CHANNELS, RATE, FORMAT, GAME_STATE, GENERAL_INPUT_STATE, set_up_stream
from input_window import InputWindow
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
    if symbol == pyglet.window.key.G:
        input_window.input_state = GAME_STATE
    if symbol == pyglet.window.key.SPACE:
        input_window.input_state = GENERAL_INPUT_STATE


@window.event
def on_draw():
    window.clear()
    # Start audio detection
    # aus audio-sample.py kopiert -----------
    data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
    # Convert audio data to numpy array
    data = np.frombuffer(data, dtype=np.int16)
    # -------------------------------------

    input_window.update(data)
    input_window.draw()


if __name__ == '__main__':
    global input_window
    input_window = InputWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
    input_window.run()
