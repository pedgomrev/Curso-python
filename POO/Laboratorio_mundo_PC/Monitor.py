class Monitor(object):
    contador_monitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño
    def __str__(self):
        return f"Monitor: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamaño}"