#!/usr/bin/python3


class Square():
    """Square class created"""    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Configure the format for print this class. """
        return "Square(width={}, height={})".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
