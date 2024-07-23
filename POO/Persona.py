class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Nombre: {self._nombre}, Edad: {self._edad}')
    def __del__(self):
        print(f'Persona: {self._nombre} eliminada')



if __name__ == '__main__':
    print('Ejecutando desde el archivo Persona')
    persona1 = Persona('Juan', 28)
    persona1.mostrar_detalles()
    persona2 = Persona('Karla', 30)
    persona2.set_edad = 33
    persona2.mostrar_detalles()
