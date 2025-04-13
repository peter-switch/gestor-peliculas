
from gestion_peliculas import GestionPeliculas
from pelicula import Pelicula

class MenuPeliculas:

    def __init__(self):
        
        self.gestionpeliculas=GestionPeliculas()

    def menu(self):

        try:

            print("\n* * * Catálogo de películas * * *")

            while True:

                print("""
1. Añadir una película
2. Listar todas las películas
3. Eliminar archivo de catálogo completo
4. Salir del sistema
                      
                      """)
                
                opcion=int(input("Selecciona opción (1-4): "))
                if opcion==1:
                    nombre_pelicula=input("\nNombre de la película: ")
                    pelicula=Pelicula(nombre_pelicula) #Importante: Crear el objeto pelicula con el nombre de la peli
                    self.gestionpeliculas.agregar_pelicula(pelicula) #llamos al método agregar_película con el objeto película
                    print("\nPelícula añadida al catálogo correctamente.")

                elif opcion==2:
                    self.gestionpeliculas.listar_peliculas()

                elif opcion==3:

                    self.gestionpeliculas.eliminar_catalogo()


                elif opcion==4:
                    print("\nSaliendo del sistema...")
                    break

                else: 
                    print("Opción incorrecta. Introduce una opción entre 1 y 4")



        except ValueError:
            print("Valor incorrecto. Introduce una opción entre 1 y 4")
        except Exception as error:
            print(f"Error en el sistema: {error}")



app=MenuPeliculas()
app.menu()