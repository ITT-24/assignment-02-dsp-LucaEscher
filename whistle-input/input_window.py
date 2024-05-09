from config import START_STATE
from input_analyzer import InputAnalyzer
import pyglet
from pynput.keyboard import Key, Controller
from rectangles import Rectangles

THRESHOLD = 100
IGNORE_DEFAULT = 0
IGNROE_TOP = 2


class InputWindow:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.batch = pyglet.graphics.Batch()
        self.input_state = START_STATE
        self.rectangles = Rectangles(self.batch, window_height, window_width).generate_rectangles()
        self.frequencies_data = []
        self.selected = 0
        self.ignore_count = IGNORE_DEFAULT
        self.keyboard = Controller()

    def update(self, data: float):
        match(self.input_state):
            case 0:
                # Start Menu
                game_label = pyglet.text.Label(text='Press G to start the game!',
                                               font_name='ARIAL',
                                               font_size=14,
                                               bold=True,
                                               x=self.window_width // 2, y=self.window_height//1.5,
                                               anchor_x='center', anchor_y='center',
                                               )

                or_label = pyglet.text.Label(text='OR',
                                             font_name='ARIAL',
                                             font_size=24,
                                             bold=True,
                                             x=self.window_width // 2, y=self.window_height//2,
                                             anchor_x='center', anchor_y='center',
                                             )

                input_label = pyglet.text.Label(text='Press SPACE to use whistle as general input!',
                                                font_name='ARIAL',
                                                font_size=14,
                                                bold=True,
                                                x=self.window_width // 2, y=self.window_height//3,
                                                anchor_x='center', anchor_y='center',
                                                )

                quit_label = pyglet.text.Label(text='(Press Q to quit)',
                                               font_name='ARIAL',
                                               font_size=10,
                                               bold=True,
                                               x=self.window_width // 2, y=self.window_height - 12,
                                               anchor_x='center', anchor_y='center',
                                               )

                game_label.draw()
                or_label.draw()
                input_label.draw()
                quit_label.draw()

            case 1:
                # Game
                data = InputAnalyzer.get_freq(data)
                self.frequencies_data.append(data)

                if len(self.frequencies_data) > 20:
                    if self.ignore_count > 0:
                        print(f'ignroing count: {self.ignore_count}')
                        self.ignore_count -= 1
                    else:
                        match(InputAnalyzer.detect_whistle(self.frequencies_data)):
                            case 0:
                                print('whistle ignored')

                            case 'rising':
                                print('UP')
                                if self.selected < 9:
                                    self.selected += 1
                                self.ignore_count = IGNROE_TOP

                            case 'falling':
                                print('DOWN')
                                if self.selected > 0:
                                    self.selected -= 1
                                self.ignore_count = IGNROE_TOP

                    self.frequencies_data = []

                for index, rectangle in enumerate(self.rectangles):
                    if index == self.selected:
                        rectangle.color = (255, 180, 9)
                    else:
                        rectangle.color = (255, 255, 255)

            case 2:
                # Geralized Input with pynput
                data = InputAnalyzer.get_freq(data)
                self.frequencies_data.append(data)

                if len(self.frequencies_data) > 20:
                    if self.ignore_count > 0:
                        print(f'ignroing count {self.ignore_count}')
                        self.ignore_count -= 1
                    else:
                        match(InputAnalyzer.detect_whistle(self.frequencies_data)):
                            case 0:
                                print('whistle ignored')

                            case 'rising':
                                print('UP')
                                # press arrow key up
                                self.keyboard.press(Key.up)
                                self.keyboard.release(Key.up)
                                self.ignore_count = IGNROE_TOP

                            case 'falling':
                                print('DOWN')
                                # press arrow key down
                                self.keyboard.press(Key.down)
                                self.keyboard.release(Key.down)
                                self.ignore_count = IGNROE_TOP

                    self.frequencies_data = []

    def draw(self):
        if self.input_state == 1:
            self.batch.draw()
        elif self.input_state == 2:
            instruction_label_title = pyglet.text.Label(text='Generalized Input on your computer:',
                                                        font_name='ARIAL',
                                                        font_size=18,
                                                        bold=True,
                                                        x=self.window_width // 2, y=self.window_height//1.5,
                                                        anchor_x='center', anchor_y='center',
                                                        )
            instruction_label_1 = pyglet.text.Label(text='- whistle up to use arrow key up',
                                                    font_name='ARIAL',
                                                    font_size=16,
                                                    bold=True,
                                                    x=self.window_width // 2, y=self.window_height//2,
                                                    anchor_x='center', anchor_y='center',
                                                    )
            instruction_label_2 = pyglet.text.Label(text='- whistle down to use arrow key down',
                                                    font_name='ARIAL',
                                                    font_size=16,
                                                    bold=True,
                                                    x=self.window_width // 2, y=self.window_height//3,
                                                    anchor_x='center', anchor_y='center',
                                                    )

            instruction_label_title.draw()
            instruction_label_1.draw()
            instruction_label_2.draw()
            

    def run(self):
        pyglet.app.run()
