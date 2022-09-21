from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setHabitat(habitat)
        self.setGenero(genero)
        self.setColorPiel(colorPiel)
        self.setVenenoso(venenoso)
        Anfibio._listado.append(self)
        super.setTotalAnimales(super.getTotalAnimales() + 1)

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def cantidadAnfibios():
        return len(Anfibio._listado)

    def movimiento():
        return "saltar"

    @staticmethod
    def crearRana(nombre, edad, genero):
        ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)