class Zoologico:
    def __init__(self, nombre, ubicacion, zona = None):
        self.setNombre(nombre)
        self.setUbicacion(ubicacion)
        self.setZona(zona)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def agregarZonas(self, zonas):
        if self.getZona() == None:
            self.setZona([])
            self._zona.append(zonas)
        else:
            self._zona.append(zonas)

    def cantidadTotalAnimales(self):
        cantidadTotalAnimales = 0
        for i in range(len(self._zona)):
            cantidadTotalAnimales = cantidadTotalAnimales + len((self.getZona())[i].getAnimales())
        return cantidadTotalAnimales