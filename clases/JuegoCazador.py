# Importamos la clase Contraseña para generar y validar contraseñas,
# las clases de Cofre para asignar recompensas o penalizaciones,
# y las excepciones personalizadas para manejar errores de entrada y validación.

from clases.Contrasena import Contraseña
from clases.Cofre import CofreMaldito, CofreComun, CofreRaro, CofreLegendario
from excepciones.errores import (
    EntradaNoNumericaError,
    LongitudInvalidaError,
    ContrasenaInvalidaError,
)


class JuegoCazador:
    """Clase que representa el flujo deljuego del cazador de contraseñas."""

    """Controla el flujo del juego, permite al jugador jugar rondas, valida erroes 
    y muestra el puntaje acumulado."""

    def __init__(self):
        """Inicializa el juego con un puntaje inicial de 0"""
        self.puntaje = 0

    def ronda(self):
        """Representa una ronda del juego, gerera una contraseña, la valida, la clasifica
        y asigna un tipo de cofre segun la calidad de la contraseña."""
        try:
            try:
                # Pide al usuario la longitud de la congraseña y valida que se un numero valido.

                longitud = int(
                    input("Ingresa la longitud de la contraseña (minimo 8): ")
                )
            except ValueError:
                raise EntradaNoNumericaError(
                    "Error: Debes ingresar un número válido (minimo 8)."
                )
            # Valida que la longitud de la contraseña sea de al menos 8 caracteres.
            if longitud < 8:
                raise LongitudInvalidaError(
                    "La longitud mínima es de 8 caracteres. Intenta nuevamente."
                )
            # Crea un objeto Contraseña y le pasa la longitud ingresada por el usuario.
            objeto = Contraseña(longitud)

            # Genera una contraseña aleatoria utilizando el método generar_contrasena del objeto Contraseña.
            clave = objeto.generar_contrasena()
            print(
                f"\nLa contraseña generada es: {clave}"
            )  # Muestra la contraseña generada.

            # Guarda y valida la contraseña utilizando el metodo valida_o_invalida del objeto Contraseña.
            validez = objeto.valida_o_invalida()

            try:
                if not validez:
                    # Si la contraseña no es válida, se lanza una excepción ContrasenaInvalidaError.
                    raise ContrasenaInvalidaError("La contraseña generada es inválida")
                # Si contraseña es valida,
                # se guarda y clasifica la contraseña utilizando el método clasificar del objeto Contraseña.
                tipo = objeto.clasificar()

                if tipo == "Media":
                    cofre = CofreComun()
                elif tipo == "Fuerte":
                    cofre = CofreRaro()
                elif tipo == "Muy fuerte":
                    cofre = CofreLegendario()
                else:
                    cofre = CofreMaldito()

            # se captura la excepción ContrasenaInvalidaError y se asigna un cofre maldito al jugador.
            except ContrasenaInvalidaError as e:
                print("Error:", e)
                cofre = CofreMaldito()

            # de acuerdo al tipo de cofre asigando se abre y suman o restan los puntos.
            puntos = cofre.abrir_cofre()
            print(
                f"\nAbriste un cofre {cofre.tipo}"
            )  # Muestra el tipo de cofre abierto.
            print(
                f"\nGanaste: {puntos} puntos"
            )  # Muestra los puntos ganados o perdidos.

            # suma los puntos obtenidos al puntaje total del jugador.
            self.puntaje += puntos

        # Captura las excepciones EntradaNoNumericaError y LongitudInvalidaError
        # para manejar errores de entrada del usuario y mostrar mensajes de error apropiados.
        except (EntradaNoNumericaError, LongitudInvalidaError) as e:
            print("Error:", e)

    def mostrar_puntaje(self):
        """Muestra el puntaje acumulado del jugador."""
        print(f"\nEstos son tus puntos actuales: {self.puntaje} puntos")

    def juego(self):
        """Controla el flujo del programa, muestra un menu de opciones
        para jugar, mostrar puntaje o salir del juego."""
        print("Bienvenido al juego Cazador de contraseñas")

        salir = False

        while not salir:
            print("\n1. Jugar")
            print("2. Mostrar puntaje")
            print("3. Salir")

            # Solicita al usuario que eliga una opcion del menu.
            # Valida que la entrada sean numeros y que sean opciones validas,
            # si no se cumple muestra un mensaje y vuelve a pedir el dato.
            try:
                opcion = int(input("Selecciona una opción: "))
            except ValueError:
                print("Error: Debes ingresar un número válido (1, 2, 3).")
                continue

            if opcion == 1:
                self.ronda()
            elif opcion == 2:
                self.mostrar_puntaje()
            elif opcion == 3:
                print(
                    f"\nGracias por jugar, tu puntaje final es: {self.puntaje} puntos"
                )
                salir = True
            else:
                print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
