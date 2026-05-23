# Permite validar longitudes de contraeñas.
class LongitudInvalidaError(Exception):
    pass


# Permite validar que la entrada del usuario sea un numero.
class EntradaNoNumericaError(Exception):
    pass


# Maneja contraseñas ivalidas que no cumplen con las condiciones de seguridad.
class ContrasenaInvalidaError(Exception):
    pass
