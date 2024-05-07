from config import RATE
import numpy as np
import pyglet
import random

# Random Werte -> entsprechen keinen tatsächlichen Noten (war nicht Teil der Anforderung ^^ )
FREQUENCY_A = 258
FREQUENCY_B = 200
FREQUENCY_C = 380
FREQUENCY_D = 350
FREQUENCY_E = 400


class Notes:

    def __init__(self, notes_batch, window_height, window_width, width) -> None:
        self.window_height = window_height
        self.window_width = window_width
        self.notes_batch = notes_batch
        self.notes_width = width
        self.notes = self.generate_notes()

    # Generiert mit ChatGPT -----
    def generate_random_frequencies(self, length):
        # Definiere die vordefinierten Frequenzen und ihre Gewichtungen
        frequencies = [FREQUENCY_A, FREQUENCY_B, FREQUENCY_C, FREQUENCY_D, FREQUENCY_E]
        weights = [1, 1, 1, 1, 1]  # gleiche Gewichtung für alle Frequenzen

        # Erzeuge ein Array mit zufälligen Frequenzen basierend auf den Gewichtungen
        random_frequencies = random.choices(frequencies, weights=weights, k=length)

        return random_frequencies
    # ---------------------------------

    def generate_notes(self):
        # Ein Stück soll 10 Noten haben
        frequencies = self.generate_random_frequencies(11)
        notes = []
        space = 120
        for index, frequency in enumerate(frequencies):
            notes.append(
                pyglet.shapes.Rectangle(
                    x=self.window_width + index * space,
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
            note.x -= 2
