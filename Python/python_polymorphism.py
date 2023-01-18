# Function overriding

from math import pi

class Shape:
    def __init__(self, name):
        self.shape_name = name

    def area(self):
        pass

    def fact(self):
        pass

    def which_shape(self):
        print("The shape is", self.shape_name)

class Square(Shape):
    def __init__(self, name, edge):
        super().__init__(name)
        self.square_side = edge

    def area(self):
        print("The area of the square is", self.square_side**2)

    def fact(self):
        print("Each angle of a square is 90 degrees and the side lengths are all equal.")
    

class Circle(Shape):
    def __init__(self, name, radius):
        self.circle_rad = radius
        super().__init__(name)
    
    def area(self):
        print("The area of the circle is", pi*(self.circle_rad**2))


sq = Square("First Square", 7.5)
cir = Circle("First Circle", 2.1)

sq.area()
sq.fact()
cir.area()

cir.which_shape()
sq.which_shape()