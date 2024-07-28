class Persona(object):
    contador_personas = 0

    def __init__(self,nombre,edad):
        Persona.contador_personas += 1
        self._id_persona = Persona.contador_personas
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Persona [{self._id_persona}, {self._nombre}, {self._edad}]'


if __name__ == '__main__':
    Persona1 = Persona('Juan', 28)
    print(Persona1)
    Persona2 = Persona('Karla', 30)
    print(Persona2)