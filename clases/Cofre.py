from abc import ABC, abstractmethod


class Cofre(ABC):
    """Clase abstracta que representa un cofre generico"""

    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def abrir_cofre(self):
        pass


class CofreMaldito(Cofre):
    """Representa un cofre maldito que resta puntos al abrirlo"""

    def __init__(self):
        """incializa el cofre maldito con el atributo tipo con el valor 'Maldito'"""
        super().__init__("Maldito")  # llama al constructor de la clase padre Cofre para
        # inicializar el atributo self.tipo con el valor "Maldito"

    def abrir_cofre(self):
        """sobrescribe el metodo abrir_cofre de la clase Cofre
        para retornar -20 puntos al abrir un cofre maldito"""
        return -20


class CofreComun(Cofre):
    """Representa un cofre común que otorga puntos al abrirlo"""

    def __init__(self):
        super().__init__("Común")  # inicializa el cofre común con el atributo
        # self.tipo con el valor 'Común'

    def abrir_cofre(self):
        """sobrescribe el metodo abrir_cofre de la clase Cofre
        para retornar 10 puntos al abrir un cofre común"""
        return 10


class CofreRaro(Cofre):
    """Representa un cofre raro que otorga más puntos al abrirlo"""

    def __init__(self):
        super().__init__("Raro")  # inicializa el cofre raro con el atributo
        # self.tipo con el valor 'Raro'

    def abrir_cofre(self):
        """sobrescribe el metodo abrir_cofre de la clase Cofre
        para retornar 25 puntos al abrir un cofre raro"""
        return 25


class CofreLegendario(Cofre):
    """Representa un cofre legendario que otorga muchos puntos al abrirlo"""

    def __init__(self):
        super().__init__("Legendario")  # inicializa el cofre legendario
        # con el atributo self.tipo con el valor 'Legendario'

    def abrir_cofre(self):
        """sobrescribe el metodo abrir_cofre de la clase Cofre
        para retornar 50 puntos al abrir un cofre legendario"""
        return 50
