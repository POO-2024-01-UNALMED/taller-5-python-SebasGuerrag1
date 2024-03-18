from zooAnimales.animal import Animal
import gestion
class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    
    def movimiento():
        return "volar"
    
    def crearHalcon( nombre, edad, genero):
        Ave.halcones+=1
        ave=Ave(nombre, edad, "montanas" , genero, "cafe glorioso")
        return ave

    def crearAguila( nombre, edad, genero):
        Ave.aguilas+=1
        ave= Ave(nombre, edad, "montanas" , genero, "blanco y amarillo")
        return ave

    
    @classmethod
    def  getListado(cls):
        return cls.listado
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,color):
        self._colorPlumas=color
    