from abc import ABC, abstractmethod


class Movable(ABC):

    @abstractmethod
    def get_velocity(self):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def set_position(self, x, y):
        pass


class Move:
    @staticmethod
    def execute(movable: Movable) -> None:
        if isinstance(movable.get_position(), (tuple, list)) and isinstance(movable.get_velocity(), (tuple, list)):
            x, y = movable.get_position()
            dx, dy = movable.get_velocity()
            movable.set_position(x+dx, y+dy)
        else:
            raise ValueError


class Rotable(ABC):

    @abstractmethod
    def get_direction(self):
        pass

    @abstractmethod
    def get_angular_velocity(self):
        pass

    @abstractmethod
    def set_direction(self, direction):
        pass

    @abstractmethod
    def get_directions_number(self):
        pass


class Rotate:
    @staticmethod
    def execute(rotable: Rotable) -> None:
        direction = rotable.get_direction()
        angle = rotable.get_angular_velocity()
        directions = rotable.get_directions_number()
        rotable.set_direction((direction+angle) % directions)





