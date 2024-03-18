from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    def _init_(self, nombre, edad, habitat, genero, colorPlumas):
        super()._init_(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    
    def movimiento():
        return "volar"
    
    @classmethod
    def crearHalcon( nombre, edad, genero):
        Ave.halcones+=1
        return Ave(nombre, edad, "montanas" , genero, "cafe glorioso")
    @classmethod
    def crearAguila( nombre, edad, genero):
        Ave.aguilas+=1
        return Ave(nombre, edad, "montanas" , genero, "blanco y amarillo")

    
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