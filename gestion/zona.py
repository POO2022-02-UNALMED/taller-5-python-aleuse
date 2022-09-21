from zooAnimales.animal import Animal
class Zona:
    def __init__(self, nombre, zoo = None, animales = None):
        self.setNombre(nombre)
        self.setZoo(zoo)
        self.setAnimales(animales)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales

    def agregarAnimales(self, animal):
        if self.getAnimales() == None:
            self.setAnimales([])
            self._animales.append(animal)
        else:
            self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)