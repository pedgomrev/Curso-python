class Orden(object):
    contador_ordenes = 0
    def __init__(self, computadores):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadores = computadores
    @property
    def computadores(self):
        return self._computadores
    @computadores.setter
    def computadores(self, computadores):
        self._computadores = computadores
    def agregar_computador(self, computador):
        self._computadores.append(computador)
    def __str__(self):
        computadores_str = ""
        for computador in self._computadores:
            computadores_str += computador.__str__() + "\n"
        return f"Orden: {self._id_orden}\n{computadores_str}"