from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None,cantidadAletas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._cantidadAletas = cantidadAletas
        self._colorEscamas= colorEscamas
        Animal.totalAnimales+=1
        Pez._listado.append(self)
    @classmethod
    def cantidadPez(cls):
        return len(cls._listado)
    
    def movimiento():
        return "nadar"
    
    def crearSalmon( nombre, edad, genero):
        Pez.salmones+=1
        return Pez(nombre, edad, "oceano" , genero, "rojo",6)
        
    def crearBacalao( nombre, edad, genero):
        Pez.bacalaos+=1
        return (nombre, edad, "oceano" , genero, "gris",6)
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,color):
        self._colorEscamas=color
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self,valor):
        self._cantidadAletas=valor
    
    @classmethod
    def setListado(cls,listado):
        cls._listado=[]
        cls._listado=listado
    def getListado(cls):
        return cls._listado