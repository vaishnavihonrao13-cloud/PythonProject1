from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        print("abstract method")


class Circle(Shape):

    def draw(self):
        super().draw()
        print("circle")


class Rectangle(Shape):

    def draw(self):
        super().draw()
        print("rectangle")

shapes=[Circle(),Rectangle()]
for shp in shapes:
    shp.draw()