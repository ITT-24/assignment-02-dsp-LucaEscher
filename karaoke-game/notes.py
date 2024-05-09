import pyglet
import random

# Random Werte -> entsprechen keinen tatsächlichen Noten (war nicht Teil der Anforderung ^^ )
FREQUENCY_A = 258
FREQUENCY_B = 200
FREQUENCY_C = 380
FREQUENCY_D = 350
FREQUENCY_E = 400

GAME_SPEED = 5
NOTE_SPACE = 150


class Notes:

    def __init__(self, notes_batch, window_height, window_width, width) -> None:
        self.window_height = window_height
        self.window_width = window_width
        self.notes_batch = notes_batch
        self.notes_width = width
        self.notes = self.generate_notes()

    # Generiert mit ChatGPT und von mir angepasst-----
    def generate_random_frequencies(self, length: int):
        frequencies = [FREQUENCY_A, FREQUENCY_B, FREQUENCY_C, FREQUENCY_D, FREQUENCY_E]
        weights = [1, 1, 1, 1, 1]
        random_frequencies = random.choices(frequencies, weights=weights, k=length)
        return random_frequencies
    # ---------------------------------

    def generate_notes(self):
        # Ein Stück soll 10 Noten haben
        frequencies = self.generate_random_frequencies(11)
        notes = []
        for index, frequency in enumerate(frequencies):
            notes.append(
                pyglet.shapes.Rectangle(
                    x=self.window_width + index * NOTE_SPACE,
                    y=frequency,
                    height=8,
                    width=self.notes_width,
                    color=(255, 255, 255),
                    batch=self.notes_batch
                )
            )
        return notes

    def start_notes(self):
        for note in self.notes:
            note.x -= GAME_SPEED
