class InvalidCommand(Exception):
    pass


class LED:
    def __init__(self, id_):
        self.id = id_

    def set_brightness(self, intensity):
        print(f'LED(id_={self.id}).set_brightness(intensity={intensity})')

    def set_color(self, red, green, blue):
        print(f'LED(id_={self.id}).set_color(' +
              f'red={red}, green={green}, blue={blue})')


class Robot:
    def __init__(self):
        self.leds = {
            1: LED(1),
            2: LED(2),
        }

    @staticmethod
    def beep(frequency, times):
        print(f'Robot.beep(frequency={frequency}, times={times})')

    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                Robot.beep(frequency, times)
            case ['NECK', angle]:
                Robot.rotate_neck(angle)
            case ['LED', id_, intensity]:
                self.leds[id_].set_brightness(intensity)
            case ['LED', id_, red, green, blue]:
                self.leds[id_].set_color(red, green, blue)
            case _:
                raise InvalidCommand(message)

    @staticmethod
    def rotate_neck(angle):
        print(f'Robot.rotate_neck(angle={angle})')
