#Creación de la clase Película
class Pelicula:

    def __init__(self, titulo):
        self.titulo = titulo
       

    def __str__(self):
        return f"Película: {self.titulo}"