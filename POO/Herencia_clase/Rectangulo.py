from FiguraGeometrica import FiguraGeometrica
from Color import Color
from Cuadrado import Cuadrado
class Rectangulo (FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    def area(self):
        return self.ancho * self.alto
    def __str__(self):
        return f'Rectangulo : {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
if __name__ == '__main__':
    rectangulo = Rectangulo(4, 8, 'Azul')
    print(rectangulo)
    print(f'Area: {rectangulo.area()}')
    print(f'Ancho: {rectangulo.ancho}')
    print(f'Alto: {rectangulo.alto}')
    print(f'Color: {rectangulo.color}')
    cuadrado = Cuadrado(4, 'Rojo')
    print(cuadrado)
    print(f'Area: {cuadrado.area()}')
    