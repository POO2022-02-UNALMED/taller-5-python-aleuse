from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setHabitat(habitat)
        self.setGenero(genero)
        self.setColorEscamas(colorEscamas)
        self.setLargoCola(largoCola)
        Reptil._listado.append(self)
        super.setTotalAnimales(super.getTotalAnimales() + 1)

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def setLargoCola(self):
        return self._largoCola

    def getLargoCola(self, largoCola):
        self._largoCola = largoCola

    def cantidadReptiles():
        return len(Reptil._listado)

    def movimiento():
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)