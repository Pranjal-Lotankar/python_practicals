'''Implement the concept of inheritance using python'''

class Shape:

    def init(self, x, y):
        self.x = x
        self.y = y

    def area(self, x, y):
        self.x = x
        self.y = y
        a = self.x * self.y
        print('Area of a rectangle', a)
ob=Shape()
ob.area(2,4)


class Square(Shape):  # class Square inherits class Shape.

    def init(self, x):
        self.x = x

    def area(self, x):
        self.x = x
        a = self.x * self.x
        print('Area of a square', a)

ob=Square()
ob.area(5)