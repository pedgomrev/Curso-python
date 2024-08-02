from Dispositivo_de_entrada import Dispositivo_de_entrada

class Raton(Dispositivo_de_entrada):
    contador_raton = 0
    def __init__(self, tipo_entrada, marca):
        Raton.contador_raton += 1
        self._id_raton = Raton.contador_raton
        super().__init__(tipo_entrada, marca)
    def __str__(self):
        return f"Raton {self._id_raton}: {super().__str__()}"
    