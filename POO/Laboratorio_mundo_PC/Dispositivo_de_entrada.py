class Dispositivo_de_entrada(object):
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca
    
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    def __str__(self):
        return f"[Dispositivo de entrada: {self._tipo_entrada}, Marca: {self._marca}]"
    