import zooAnimales
import gestion

class Animal:
    _totalAnimales=0
    def __init__ (self,nombre, edad,habitat,genero,zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal._totalAnimales +=1

    def movimiento(self):
        return "Desplazarse"
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : "+str(zooAnimales.mamifero.Mamifero.cantidadMamiferos())+"\n"+"Aves : "+str(zooAnimales.ave.Ave.cantidadAves())+"\n"+"Reptiles : "+str(zooAnimales.reptil.Reptil.cantidadReptiles())+"\n"+"Peces : "+str(zooAnimales.pez.Pez.cantidadPeces())+"\n"+"Anfibios : "+str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())

    def __str__(self):
        string = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        if self._zona != None:
            string += f", la zona en la que me ubico es {self._zona}, en el {self._zoo}"
        return string

    
    def toString(self):
        return self.__str__()

    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    def setTotalAnimales(cls,numero):
        cls._totalAnimales=numero

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