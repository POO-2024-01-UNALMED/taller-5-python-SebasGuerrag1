class Zoologico:
    _zonas=[]
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
    

    @classmethod    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        Animalitos=0
        for i in self._zonas:
            Animalitos+=i.cantidadAnimales()
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre= nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    
    def getZonas(self):
        return self._zonas
    
    def setZonas(self,zonas):
        self._zonas=zonas



