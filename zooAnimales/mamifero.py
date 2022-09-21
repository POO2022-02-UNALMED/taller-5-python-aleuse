from zooAnimales.animal import Animal
class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setHabitat(habitat)
        self.setGenero(genero)
        self.setPelaje(pelaje)
        self.setPatas(patas)
        Mamifero._listado.append(self)
        super.setTotalAnimales(super.getTotalAnimales() + 1)

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    def cantidadMamiferos():
        return len(Mamifero._listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)