# Assignment 2

# Installation
```
pip install -r requirements.txt
```

## Troubleshooting
If you are on a mac you might to install portaudio first to your device in order to use PyAudio.
It also might help to install pyAudio with sudo instead of pip.

# Karaoke Game

## Start the game
```
python3 karaoke-game/karaoke.py
```

1. Select your audio device
2. Sing and hit the notes

(You can always press Q to quit the game)

# Whistle Input

## Start the code
```
python3 whistle-input/whistle-input.py
```
1. Select your audio device
2. Select a game mode:

    - Press G to play a little game where you can select squares with a whistle up or whistle down
    - Press SPACE to trigger your arrow key up and down with a whistle up or down. And then have fun scrolling over your pdf via whistling 

(You can always press Q to quit the code)

## User feedback

In order to see what is going on in the background the terminal prints if a input is ignored because it is not identified as a whistle down or up, if it detected a whistle up or if it detected a whistle down. Also the square which is selected is of course highlighted.

## Latency disclaimer

In detecting your voice there should be none. However if a whistle up or down is detected, the whistle detection will pause for 20 frequencies (shown with: "ingoring count: -number-") before it is hearing for the next one. This is integrated to prevent the user from accidentaly triggering too many whistle ups or down at once. By doing this the user stays in controll.


# Disclaimer classes

I'm aware that config.py, for example, exists in both directories and is very similar. One could have called this script from a different directory, e.g. from the karaoke folder. However, I thought that a complete task should be contained in one folder. That's why this script is more or less duplicated here. If this approach is not correct, please mention it in the feedback, but please no point deduction ;)
