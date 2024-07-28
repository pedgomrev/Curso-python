from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @abstractmethod
    def area(self):
        pass
    def __str__(self):
        return f'Ancho: {self.ancho}, Alto: {self.alto}'
    
    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho):
        if ancho <= 0:
            raise ValueError('Ancho debe ser mayor a 0')
        self.__ancho = ancho
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto):
        if alto <= 0:
            raise ValueError('Alto debe ser mayor a 0')
        self.__alto = alto
