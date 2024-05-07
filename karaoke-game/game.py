from config import RATE
import math
import numpy as np
from notes import Notes
from player import Player
import pyglet
# from score import Score


class Game:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.batch = pyglet.graphics.Batch()
        self.notes_batch = pyglet.graphics.Batch()
        self.player = Player(self.batch, window_height)
        self.notes = Notes(self.notes_batch, window_height, window_width, 50)
        self.score = 0
        self.game_state = 0

    # Generiert mit ChatGPT und angepasst von mir ------------

    # useful souce: https://stackoverflow.com/questions/59979354/what-is-the-difference-between-numpy-fft-fft-and-numpy-fft-fftfreq
    def get_freq(self, data, threshold=100):
        # don't react to background noise
        if np.max(np.abs(data)) > threshold:
            fft_data = np.abs(np.fft.fft(data))
            frequency_bins = np.fft.fftfreq(len(fft_data), d=1/RATE)
            major_frequency = np.abs(frequency_bins[np.argmax(fft_data)])
            return np.round(major_frequency, 1)
        return 0
    # -----------------------------------

    def update(self, data):
        match(self.game_state):
            case 0:
                start_label = pyglet.text.Label(text='Press SPACE to start!',
                                                font_name='ARIAL',
                                                font_size=24,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//2,
                                                anchor_x='center', anchor_y='center',
                                                )
                start_label.draw()

            case 1:
                # Player
                pos_y = self.player.body.y
                if pos_y < 0:
                    pos_y = 0
                # check window borders
                elif pos_y < self.window_height - self.player.body.height:
                    audio_data = self.get_freq(data)
                    self.player.update(audio_data)
                else:
                    audio_data = self.get_freq(data)

                # Notes
                self.notes.start_notes()

                # Check collisions
                for note in self.notes.notes:

                    if note.x >= self.player.body.x - 15 and note.x <= self.player.body.x + 4:
                        if note.y <= self.player.body.y + 15 and note.y >= self.player.body.y - 15:
                            note.color = (100, 200, 150)
                            self.score += 10

                if self.notes.notes[10].x + self.notes.notes_width <= 0:
                    self.game_state = 2

            case 2:
                end_label = pyglet.text.Label(text=f'Final Score: {self.score}',
                                              font_name='ARIAL',
                                              font_size=24,
                                              bold=True,
                                              x=self.window_width//2, y=self.window_height//2,
                                              anchor_x='center', anchor_y='center',
                                              )
                end_label.draw()

    def draw(self):
        score_label = pyglet.text.Label(text=f'Score: {self.score} \t (Press Q to Quit)',
                                        font_name='Arial',
                                        font_size=15,
                                        bold=True,
                                        x=self.window_width - (self.window_width - 10), y=self.window_height - 22, batch=self.batch)

        self.batch.draw()
        self.notes_batch.draw()

    def run(self):
        pyglet.app.run()
