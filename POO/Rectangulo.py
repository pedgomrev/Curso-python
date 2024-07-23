class Rectangulo():
    """
    Clase que representa un rectángulo.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * self.base + 2 * self.altura
    
"""
Test de la clase Rectangulo
"""
input_base = int(input('Proporciona la base: '))
input_altura = int(input('Proporciona la altura: '))
rectangulo = Rectangulo(input_base, input_altura)
print(f'Área: {rectangulo.area()}')
print(f'Perímetro: {rectangulo.perimetro()}')