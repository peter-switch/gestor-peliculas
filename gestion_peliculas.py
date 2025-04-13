import os

class GestionPeliculas:

    def __init__(self):
       self.nombre_archivo="peliculas.txt"

    def agregar_pelicula(self,pelicula):
        with open(self.nombre_archivo, "a", encoding="utf8") as archivo:
            #archivo.write(pelicula.titulo) De este modo escribe cada vez sin salto de línea
            archivo.write(f"{pelicula.titulo}\n") #De este modo, cada película irá en una línea distinta



    def listar_peliculas(self):
        with open(self.nombre_archivo, "r", encoding="utf8") as archivo:
            print("\n* * * Listado de Películas * * *\n")
            print(archivo.read())
    

    def eliminar_catalogo(self):
        os.remove(self.nombre_archivo)
        print(f"\nCatalogo eliminado correctamente.")
    




