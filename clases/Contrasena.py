import random
import string


class Contraseña:
    """Clase para generar y validar contraseñas."""

    def __init__(self, longitud):
        """Inicializa la clase conla longitud y los caracteres permitidos."""
        self.longitud = longitud
        self.caracter_especial = "¿¡?=)(/¨*+-%&$#!."
        self.caracteres = string.ascii_letters + string.digits + self.caracter_especial
        self.password = None

    def generar_contrasena(self):
        """Genera y retorna una contraseña aleatoria con la longitud ingresada en
        el objeto de la clase y los caracteres permitidos."""
        self.password = ""

        for letras in range(self.longitud):
            self.password += random.choice(self.caracteres)

        return self.password

    def validar_longitud(self):
        """Valida que los caracteres de la contraseña sean al menos 8."""
        return len(self.password) >= 8

    def validar_mayuscula(self):
        """Valida que la contraseña contenga al menos una letra mayúscula."""
        for letra in self.password:
            if letra.isupper():
                return True
        return False

    def validar_minuscula(self):
        """Valida que la contraseña contenga al menos una letra minúscula."""
        for letra in self.password:
            if letra.islower():
                return True
        return False

    def validar_numero(self):
        """Valida que la contraseña contenga al menos un número."""
        for letra in self.password:
            if letra.isdigit():
                return True
        return False

    def validar_caracter_especial(self):
        """Valida que la contraseña contenga al menos un carácter
        especial de la lista de caracteres especiales permitidos."""
        for letra in self.password:
            if letra in self.caracter_especial:
                return True
        return False

    def validar_caracter_repetido(self):
        """Valida que la contraseña no contenga caracteres repetidos."""
        return len(self.password) == len(set(self.password))

    def valida_o_invalida(self):
        """Valida que la contraseña cumpla con todas las condiciones
        de seguridad anteriores y retorna True si es válida o False si es inválida."""
        return (
            self.validar_longitud()
            and self.validar_mayuscula()
            and self.validar_minuscula()
            and self.validar_numero()
            and self.validar_caracter_especial()
            and self.validar_caracter_repetido()
        )

    def calcular_puntos(self):
        """Calcula que tan fuerte es la contraseña y retorna
        los puntos obtenidos según las condiciones de seguridad anteriores."""
        if self.valida_o_invalida():
            puntos = 0

            # Longitud mínima
            if len(self.password) >= 8:
                puntos += 1

            # Longitud extra se considera un punto adicional.
            if len(self.password) > 8:
                puntos += 1
            # Debe contener minimo una mayuscula.
            if self.validar_mayuscula():
                puntos += 1
            # Debe contener minimo una minuscula.
            if self.validar_minuscula():
                puntos += 1
            # Debe contener minimo un numero.
            if self.validar_numero():
                puntos += 1
            # Debe contener minimo un carácter especial.
            if self.validar_caracter_especial():
                puntos += 1
            # No debe contener caracteres repetidos.
            if self.validar_caracter_repetido():
                puntos += 1

            # Más de 1 carácter especial diferente se considera un punto adicional.
            especiales = 0
            for caracter in self.password:
                if caracter in self.caracter_especial:
                    especiales += 1

            if especiales > 1:
                puntos += 1

            return puntos
        # Si la contraseña no es válida no se le asignan puntos y se considera inválida.
        else:
            return "Inválida"

    def clasificar(self):
        """Toma los puntos obtenidos por la contraseña en calcular_puntos y retorna
        su clasificación según la cantidad de puntos obtenidos."""
        puntos = self.calcular_puntos()

        if puntos == 6:
            return "Media"
        elif puntos == 7:
            return "Fuerte"
        else:
            return "Muy fuerte"
