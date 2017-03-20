class Position2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)

    @staticmethod
    def from_morse(morse_position):
        x = morse_position['x']
        y = morse_position['y']
        return Position2D(x, y)