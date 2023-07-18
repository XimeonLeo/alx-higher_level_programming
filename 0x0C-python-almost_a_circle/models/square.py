#!/usr/bin/python3
""" A module that defines a subclass that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A sub-class, inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the attributes for square """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the value for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size> """
        idd = self.id
        xx = self.x
        yy = self.y
        sizze = self.height
        return f"[Square] ({idd}) {xx}/{yy} - {sizze}"

    def update(self, *args, **kwargs):
        """ Updates the value for Square attributes """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Returns the attributes of a Square in a Dict """
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
