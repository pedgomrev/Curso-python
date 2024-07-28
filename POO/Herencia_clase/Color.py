class Color(object):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return f'Color: {self.color}'
    
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
