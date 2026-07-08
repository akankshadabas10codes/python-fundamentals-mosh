# Classes
# class is a blueprint for creating new objects
# object: instance of a class
# Class: Human  (that has all the attributes of a human)
# Objects: John, Mary...

## Creating classes
## Constructor


class Point:
    # this
    # in this block we will define all the functions related to points
    # Thie magic method is called a constructor and when we creare
    # a new point object.
    # Self is a reference to a current point object.
    # When we call the point class, python will itnernally create
    # the point object in memory an dset itself in reference to that point obejct.
    # this point object will have certain methods. point will also have attributes which are variables that include data about that object.
    # #
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# when we create an initial point object we wantt o suppley the x and y values
# to achieve this we need a constructor which is a special method that is called when
# we create a new point object
point = Point(1, 2)
print(point.draw)
# print(type(point))
# # to check if this object is an instance of a class
# print(isinstance(point, Point))
