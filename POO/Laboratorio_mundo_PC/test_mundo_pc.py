from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computador import Computador
from Orden import Orden

if __name__ == '__main__':
    monitor1 = Monitor("HP", 15)
    teclado1 = Teclado("USB", "Genius")
    raton1 = Raton("USB", "Genius")
    computador1 = Computador("HP", monitor1, teclado1, raton1)
    monitor2 = Monitor("Acer", 27)
    teclado2 = Teclado("Bluetooth", "Acer")
    raton2 = Raton("Bluetooth", "Acer")
    computador2 = Computador("Acer", monitor2, teclado2, raton2)
    orden1 = Orden([computador1, computador2])
    print(orden1)
    orden2 = Orden([computador2])
    print(orden2)
    orden3 = Orden([])
    print(orden3)