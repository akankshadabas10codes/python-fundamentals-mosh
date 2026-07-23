# Classes
# class is a blueprint for creating new objects
# object: instance of a class
# Class: Human  (that has all the attributes of a human)
# Objects: John, Mary...

## Creating classes
## Constructor


class Point:
    # class level attribute:
    # they are shared across all instances of a class.
    # if we chnage their values, the change is visible to all object of that type.
    default_color = "red"

    # this
    # in this block we will define all the functions related to points
    # Thie magic method is called a constructor and when we creare
    # a new point object.
    # Self is a reference to a current point object.
    # When we call the point class, python will itnernally create
    # the point object in memory an dset itself in reference to that point obejct.
    # this point object will have certain methods. point will also have attributes which are variables that include data about that object.
    # This is an exmample of an instance method #
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # this is also an instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# if we try to change a default color
# we are using point class here:
Point.default_color = "yellow"
# when we create an initial point object we wantt o suppley the x and y values
# to achieve this we need a constructor which is a special method that is called when
# we create a new point object
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()
# we can also define attributes later on like this below
# all these attributes that we have defined like x, y and z. these are
# all instance attributes, in the sense that these all belong to the point instance/ point objects.
another = Point(3, 4)
print(another.default_color)
another.draw()
# print(type(point))
# # to check if this object is an instance of a class
# print(isinstance(point, Point))
