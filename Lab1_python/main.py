from Geometric_shapes.Figures import Figures
from Geometric_shapes.Figures_on_the_plane import Triangle, Circle
from Geometric_shapes.Figures_in_space import Three_dimensional_figures, Cylinder

if __name__ == '__main__':
    figure = Figures("circle")
    figure.calculate_square("circle")

    circle = Circle("circle", True, 2)
    circle.calculate_square("circle", 1)
    circle.print_type_figure("circle")
    print("\n")

    triangle = Triangle("triangle", True, 2, 2)
    triangle.calculate_square("triangle", 2, 2)
    triangle.print_type_figure("triangle")
    print("\n")

    cylinder = Cylinder("cylinder", True, True, 1, 1)
    cylinder.calculate_square("cylinder")
    cylinder.print_volume("cylinder", 1, 1)
    print("\n")

    просторова_фігура = Three_dimensional_figures("фігура", True)
    просторова_фігура.calculate_square("фігура")
    просторова_фігура.print_volume("фігура", True)


