class Computador(object):
    contador_computadores = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computador.contador_computadores += 1
        self._id_computador = Computador.contador_computadores
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    def __str__(self):
        return f"Computador {self._id_computador}: {self._nombre}\n{self._monitor}\n{self._teclado}\n{self._raton}"