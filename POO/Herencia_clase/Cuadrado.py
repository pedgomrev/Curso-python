from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado (FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.ancho * self.alto
    def __str__(self):
        return f'Cuadrado : {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}' 
    
if __name__ == '__main__':
    cuadrado = Cuadrado(4, 'Rojo')
    print(cuadrado)
    print(f'Area: {cuadrado.area()}')