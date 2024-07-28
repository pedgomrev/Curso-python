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
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalles(self):
        print(f'Nombre: {self._nombre}, Edad: {self._edad}')

    def __str__(self) -> str:
        return f'Nombre: {self._nombre}, Edad: {self._edad}'
    def __del__(self):
        print(f'Persona: {self._nombre} eliminada')

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f'Sueldo: {self._sueldo}')
    
    def __str__(self) -> str:
        return super().__str__() + f', Sueldo: {self._sueldo}'
    def __del__(self):
        print(f'Empleado: {self._nombre} eliminado')

if __name__ == '__main__':
    print('Ejecutando desde el archivo Persona/Empleado')
    persona1 = Persona('Juan', 28)
    persona1.mostrar_detalles()
    persona2 = Persona('Karla', 30)
    persona2.set_edad = 33
    persona2.mostrar_detalles()
    empleado1 = Empleado('Laura', 35, 5000)
    empleado1.mostrar_detalles()
    print(empleado1)
    print(persona1)
