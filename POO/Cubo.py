class Cubo():
    """
    Clase que representa un cubo.
    """
    def __init__(self,ancho,alto,profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    def volumen(self):
        return self.ancho * self.alto * self.profundo
    def area(self):
        return 2 * (self.ancho * self.alto + self.ancho * self.profundo + self.alto * self.profundo)

"""
Test de la clase Cubo
"""
input_ancho = int(input('Proporciona el ancho: '))
input_alto = int(input('Proporciona el alto: '))
input_profundo = int(input('Proporciona el profundo: '))
cubo = Cubo(input_ancho, input_alto, input_profundo)
print(f'Volumen: {cubo.volumen()}')