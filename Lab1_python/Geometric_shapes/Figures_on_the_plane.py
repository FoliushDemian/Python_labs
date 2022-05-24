from Geometric_shapes.Figures import Figures
import math


class Flat_figures(Figures):
    def __init__(self, name: str, can_calculate_square: bool):
        super().__init__(name)
        self.can_calculate_square = can_calculate_square

    def print_type_figure(self, name):
        print(f'{name} is a flat figure')


class Circle(Flat_figures):
    def __init__(self, name: str, can_calculate_square: bool, radius_in_centimeters: int):
        super().__init__(name, can_calculate_square)
        self.radius_in_centimeters = radius_in_centimeters

    def calculate_square(self, name: str, radius_in_centimeters: int):
        print(f'{name} has an area', math.pi * (radius_in_centimeters ** 2))


class Triangle(Flat_figures):
    def __init__(self, name: str, can_calculate_square: bool, height: int, side: int):
        super().__init__(name, can_calculate_square)
        self.height = height
        self.side = side

    def calculate_square(self, name: str, height: int, side: int):
        print(f'{name} has an area', 0.5 * height * side)
