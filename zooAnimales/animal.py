import gestion
import zooAnimales
class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setHabitat(habitat)
        self.setGenero(genero)
        self.setZona(zona)
        Animal.setTotalAnimales(Animal.getTotalAnimales() + 1)

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def movimiento():
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        cadena = (f"Mamiferos: {len(zooAnimales.mamifero.Mamifero.getListado())} \n Aves: {len(zooAnimales.ave.Ave.getListado())} \n Reptiles: {len(zooAnimales.reptil.Reptil.getListado())} \n Peces: {len(zooAnimales.pez.Pez.getListado())} \n Anfibios {len(zooAnimales.anfibio.Anfibio.getListado())}")
        return cadena

    def toString(self):
        if Animal.getZona() != None:
            return (f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en la que me ubico es {self.getZona()}, en el zoo {self.getZona().getZoo().getNombre()}")
        else:
            return (f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}")