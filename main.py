# Importamos la clase principal del juego.
from clases.JuegoCazador import JuegoCazador

# Si el nombre del modulo es el principal, se crea una instancia de JuegoCazador
# y se llama al metodo juego para iniciar el juego.
if __name__ == "__main__":
    juego = JuegoCazador()
    juego.juego()
