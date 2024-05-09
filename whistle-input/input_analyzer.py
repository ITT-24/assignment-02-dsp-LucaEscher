from config import RATE
import numpy as np

THRESHOLD = 100
FREQUENCY_THRESHOLD = 400


class InputAnalyzer:

    def __init__(self) -> None:
        pass

    # Generiert mit ChatGPT und angepasst von mir ------------
    # Von mir selbst aus karaoke-game kopiert -> man könnte auch referenzieren aber ich dachte, dass eine Abgabe immer komplett in einem Ordner sein sollte

    # useful souce: https://stackoverflow.com/questions/59979354/what-is-the-difference-between-numpy-fft-fft-and-numpy-fft-fftfreq
    def get_freq(data: list):
        # don't react to background noise
        if np.max(np.abs(data)) > THRESHOLD:
            fft_data = np.abs(np.fft.fft(data))
            frequency_bins = np.fft.fftfreq(len(fft_data), d=1/RATE)
            major_frequency = np.abs(frequency_bins[np.argmax(fft_data)])
            return np.round(major_frequency, 1)
        return 0
    # -----------------------------------

    def detect_whistle(frequencies: list):
        if sum(frequencies) > FREQUENCY_THRESHOLD:
            # check if values rising
            is_rising = all(frequencies[i] <= frequencies[i+1] for i in range(len(frequencies)-1))
            # check if values falling
            is_falling = all(frequencies[i] >= frequencies[i+1] for i in range(len(frequencies)-1))
            # at lesat 4 values should rise or fall
            if is_rising and frequencies.count(0) <= 6:
                return 'rising'
            elif is_falling and frequencies.count(0) <= 6:
                return 'falling'
            else:
                return 0
        else:
            return 0
