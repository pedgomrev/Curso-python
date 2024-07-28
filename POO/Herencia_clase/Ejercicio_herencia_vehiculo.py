class Vehiculo(object):
    def __init__ (self,ruedas,color):
        self.ruedas = ruedas
        self.color = color
    def __str__(self):
        return f'Vehiculo: ruedas: {self.ruedas}, color: {self.color}'
    
class Coche(Vehiculo):
    def __init__ (self,ruedas,color,velocidad):
        super().__init__(ruedas,color)
        self.velocidad = velocidad
    def __str__(self):
        return f'Coche: ruedas:{self.ruedas}, color: {self.color}, velocidad: {self.velocidad}'
    
class Bicicleta(Vehiculo):
    def __init__ (self,ruedas,color,tipo):
        super().__init__(ruedas,color)
        self.tipo = tipo
    def __str__(self):
        return f'Bicicleta: ruedas:{self.ruedas}, color: {self.color}, tipo: {self.tipo}'

if __name__ == '__main__':
    vehiculo = Vehiculo(4,'rojo')
    print(vehiculo)
    coche = Coche(4,'azul',150)
    print(coche)
    bicicleta = Bicicleta(2,'verde','urbana')
    print(bicicleta)
    print(isinstance(vehiculo,Vehiculo))
    print(isinstance(coche,Coche))
    print(isinstance(coche,Vehiculo))
    print(isinstance(bicicleta,Bicicleta))
    print(isinstance(bicicleta,Vehiculo))
    print(isinstance(vehiculo,Coche))
    print(isinstance(vehiculo,Bicicleta))
    print(isinstance(coche,Bicicleta))
    print(isinstance(bicicleta,Coche))