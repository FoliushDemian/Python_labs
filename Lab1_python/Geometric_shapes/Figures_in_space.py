from Geometric_shapes.Figures import Figures
import math


class Three_dimensional_figures(Figures):
    def __init__(self, name: str, can_calculate_volume: bool):
        super().__init__(name)
        self.can_calculate_volume = can_calculate_volume

    def print_volume(self, name: str, can_calculate_volume: bool):
        print(f'we can find volume for {name}, because can_calculate_volume is {can_calculate_volume}')


class Cylinder(Three_dimensional_figures):
    def __init__(self, name: str, can_calculate_volume: bool, side_surface_is_rectangle: bool,
                 radius_in_centimeters: int, height: int):
        super().__init__(name, can_calculate_volume)
        self.side_surface_is_rectangle = side_surface_is_rectangle
        self.radius_in_centimeters = radius_in_centimeters
        self.height = height

    def print_volume(self, name: str, radius_in_centimeters: int, height: int):
        print(f'{name} has a volume', height * math.pi * (radius_in_centimeters ** 2))


class Cone(Three_dimensional_figures):
    def __init__(self, name: str, can_calculate_volume: bool, side_surface_is_segment: bool, radius_in_centimeters: int,
                 height: int):
        super().__init__(name, can_calculate_volume)
        self.side_surface_is_segment = side_surface_is_segment
        self.radius_in_centimeters = radius_in_centimeters
        self.height = height

    def print_volume(self, name: str, radius_in_centimeters: int, height: int):
        print(f'{name} has a volume', 0.33 * height * math.pi * (radius_in_centimeters ** 2))


class Sphere(Three_dimensional_figures):
    def __init__(self, name: str, can_calculate_volume: bool, side_surface_is_circle: bool, radius_in_centimeters: int):
        super().__init__(name, can_calculate_volume)
        self.side_surface_is_circle = side_surface_is_circle
        self.radius_in_centimeters = radius_in_centimeters

    def print_volume(self, name: str, radius_in_centimeters: int):
        print(f'{name} has a volume', 1.33 * math.pi * (radius_in_centimeters ** 3))

