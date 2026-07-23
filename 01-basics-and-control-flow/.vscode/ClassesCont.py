## Class vs instance methods
# In the example above, both the init and draw are instance methods. so we can call them  using an instance
# of the point class, using an object. We use these instance methods whenever we ned a object reference, for example
# when drawing a point, you really need work with a specific point object. That is why this draw method
# is defined as an instance method. But there are times that you don't really need an existing object, and that's when we use a class
# method. #

# For example we want to create a point object as:
# point = Point (0,0)
# we can use the class reference and use the .zero method.
# Point.zero()
# In this example we refer this zero method as a factory method, it creates a new object. #


class Pointer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # we use a decorator and it is a way to extend the behavior of a method or function.
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


pointer = Pointer.zero()
print(str(pointer))
pointer.draw()


## Magic methods have 2 underlines at the beginning of their name and they are
# called automatically by python interpreter
## init and str are 2 magic mathods


## Comparing objects
class Pointed:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Pointed(self.x + other.x, self.y + other.y)


pointed = Pointed(10, 20)
other = Pointed(1, 2)
# print(pointed == other)
print(pointed > other)  # returns error unlessw we defne it as a magic method
print(pointed < other)
combined = pointed + other
print(combined.x)
# if we have 2 different point objects with the same values and we compare them
# we get false because, by default, this equality operator compares the references and addresses
# of these 2 objects in memory. in this case these 2 vars are ref 2 different objects in memory
# and that's why they are not equal #


## Supporting arithmetic operations
## creating custom containers
class TagCloud:
    def __init__(self):
        self.__tags = {}

    # Look for tag in the dictionary.
    # Get its current count.
    # If the tag does not exist, use 0.
    # Add 1.
    # Store the new count. #
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.__tags["PYTHON"])
print(cloud.__dict__)
# On a Mac:
# Select text character by character: Shift + Left/Right Arrow
# Select one word at a time: Option + Shift + Left/Right Arrow
# Select to the beginning or end of the line: Command + Shift + Left/Right Arrow
# Select everything: Command + A
# In VS Code, to move a selected line up or down:
# Option + Up Arrow
# Option + Down Arrow


class Product:
    def __init__(self, price):
        self.__price = price

    def gert_price(self):
        return self.__price


product = Product(-50)
