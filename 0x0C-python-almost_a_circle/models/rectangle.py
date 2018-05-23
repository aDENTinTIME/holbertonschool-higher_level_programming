#!/usr/bin/python3
"""Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from class Base.
    A rectangle object that can create a rectangle of any size.
    It can return it's area or print a 2D representation
    of itself at a given offset.


    Args:
        width: Length of rectangle's width.
        height: Length of rectangle's height.
        x: Horizontal offset to print at.
        y: Vertical offset to print at.
        id: This is handled by the super-class Base.
            The desired ID of an object's instance, or the next available ID.
    """
    def errCheck(self, name, value):
        """
        Error checking method that will raise appropriate
        error/message combos.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.errCheck("width", width)
        self.errCheck("height", height)
        self.errCheck("x", x)
        self.errCheck("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        atts = ["id", "width", "height", "x", "y"]
        [setattr(self, a, b) for a, b in zip(atts, args)]
        [setattr(self, a, b) for a, b in kwargs.items()]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.errCheck("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.errCheck("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.errCheck("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.errCheck("y", value)
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        [print() for a in range(self.y)]
        [print("" * self.x, "#" * self.width) for x in range(self.height)]

    def to_dictionary(self):
        """Alternate non-one line solution
        hold = {}
        for key, val in self.__dict__.items():
            if key.find("__") != -1:
                key = key[key.find("__")+2:]
            hold[key] = val
        return hold
        """
        return dict((key[key.find("__")+2:]
                    if key.find("__") != -1 else key, val)
                    for key, val in self.__dict__.items())
