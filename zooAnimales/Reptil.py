from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado=[]
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None,largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._largoCola = largoCola
        self._colorEscamas= colorEscamas
        
        Reptil._listado.append(self)
    @classmethod
    def cantidadReptil(cls):
        return len(cls._listado)
    
    def movimiento():
        return "reptar"
    @classmethod
    def crearIguana( nombre, edad, genero):
        Reptil.iguanas+=1
        return Reptil(nombre, edad, "humedal" , genero, "verde",3)
    @classmethod
    def crearSerpiente( nombre, edad, genero):
        Reptil.serpientes+=1
        return (nombre, edad, "jungla" , genero, "blanco",1)
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,color):
        self._colorEscamas=color
    
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,valor):
        self._largoCola=valor
    
    @classmethod
    def setListado(cls,listado):
        cls._listado=[]
        cls._listado=listado
    def getListado(cls):
        return cls._listado