class Command:
    def __init__(self, motor, direction, error=False):
        self.motor = motor
        self.direction = direction
        self.error = error
