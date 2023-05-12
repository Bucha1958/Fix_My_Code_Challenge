#!/usr/bin/python3


class Square():
    """Square class created"""    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        if args:
            try:
                self.width, self.height = args
            except:
                raise ValueError
        else:
            try:
                self.width = kwargs.get("width")
                self.height = kwargs.get("height")
            except:
                raise ValueError
        
        if self.width != self.height:
                raise ValueError

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

    s = Square(width=12, height=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
