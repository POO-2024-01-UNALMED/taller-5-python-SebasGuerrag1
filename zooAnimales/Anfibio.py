from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso= venenoso
        Anfibio._listado.append(self)
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento():
        return "Saltar"
    
    def crearRana( nombre, edad, genero):
        Anfibio.ranas+=1
        return Anfibio(nombre, edad, "selva" , genero, "rojo",True)
        
    def crearSalamandra( nombre, edad, genero):
        Anfibio.ranas+=1
        return Anfibio(nombre, edad, "selva" , genero, "negro y amarillo",False)
    
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,color):
        self._colorPiel=color
    
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,valor):
        self._venenoso=valor
    
    @classmethod
    def setListado(cls,lista):
        cls._listado=lista
    def getListado(cls):
        return cls._listado
    
