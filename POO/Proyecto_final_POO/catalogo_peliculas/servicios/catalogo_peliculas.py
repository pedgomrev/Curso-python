

class CatalogoPeliculas(object):
    ruta_archivo = "POO\Proyecto_final_POO\pelicula.txt"
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")
            print(f"Se ha agregado la pelicula: {pelicula.nombre}")
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catalogo de peliculas:".center(50, "-")) 
            print(archivo.read())
    @classmethod
    def eliminar_peliculas(cls):
        with open(cls.ruta_archivo, "w", encoding="utf8") as archivo:
            archivo.write("")
            print("Se ha eliminado el archivo de peliculas")