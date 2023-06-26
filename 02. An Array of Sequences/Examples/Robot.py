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
        # The expression after the match keyword is the subject. The subject is
        # the data that Python will try to match to the patterns in each case
        # clause.
        match message:
            # This pattern matches any subject that is a sequence with three
            # items. The first item must be the string 'BEEPER'. The second and
            # third item can be anything, and they will be bound to the
            # variables frequency and times, in that order.
            case ['BEEPER', frequency, times]:
                Robot.beep(frequency, times)
            # This matches any subject with two items, the first being 'NECK'.
            case ['NECK', angle]:
                Robot.rotate_neck(angle)
            # This will match a subject with three items starting with 'LED'.
            # If the number of items does not match, Python proceeds to the
            # next case.
            case ['LED', id_, intensity]:
                self.leds[id_].set_brightness(intensity)
            # Another sequence pattern starting with 'LED', now with five
            # items–including the 'LED' constant.
            case ['LED', id_, red, green, blue]:
                self.leds[id_].set_color(red, green, blue)
            # This is the default case. It will match any subject that did not
            # match a previous pattern. The _ variable is special.
            case _:
                raise InvalidCommand(message)

    @staticmethod
    def rotate_neck(angle):
        print(f'Robot.rotate_neck(angle={angle})')
