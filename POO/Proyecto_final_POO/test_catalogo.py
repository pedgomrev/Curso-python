from catalogo_peliculas.servicios.catalogo_peliculas import CatalogoPeliculas as cp
from catalogo_peliculas.dominio.pelicula import Pelicula

opcion = None
while opcion != 4:
    try:
        print("Opciones:")
        print("1. Agregar pelicula")
        print("2. Listar peliculas")
        print("3. Eliminar peliculas")
        print("4. Salir")
        opcion = int(input("Escribe tu opcion (1-4): "))
    except Exception as e:
        print(f"Error: {e}")
        opcion = None
    if opcion == 1:
        nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        cp.agregar_pelicula(pelicula)
    elif opcion == 2:
        cp.listar_peliculas()
    elif opcion == 3:
        cp.eliminar_peliculas()

else:
    print("Saliendo del programa")