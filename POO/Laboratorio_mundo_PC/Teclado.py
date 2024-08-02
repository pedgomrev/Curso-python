from Dispositivo_de_entrada import Dispositivo_de_entrada

class Teclado(Dispositivo_de_entrada):
    contador_teclados = 0
    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipo_entrada, marca)
    def __str__(self):
        return f"Teclado {self._id_teclado}: {super().__str__()}"