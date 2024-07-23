class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de suma, resta, etc.
    """
    def __init__(self,opA,opB):
        self.opA = opA
        self.opB = opB
    def suma(self):
        return self.opA + self.opB
    def resta(self):
        return self.opA - self.opB
    def division(self):
        return self.opA / self.opB
    def multiplicacion(self):
        return self.opA * self.opB
    
"""
Test de la clase Aritmetica
"""
aritmetica = Aritmetica(5,3)
summa = Aritmetica(5,3).suma()
resta = Aritmetica(5,3).resta()
division = Aritmetica(5,3).division()
multiplicacion = Aritmetica(5,3).multiplicacion()

print(f"summa de {aritmetica.opA} y {aritmetica.opB}: {summa}")
print(f"resta de {aritmetica.opA} y {aritmetica.opB}: {resta}")
print(f"division de {aritmetica.opA} y {aritmetica.opB}: {division}")
print(f"multiplicacion de {aritmetica.opA} y {aritmetica.opB}: {multiplicacion}")