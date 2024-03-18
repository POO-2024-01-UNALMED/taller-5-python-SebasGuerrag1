import Anfibio
import Ave
import Mamifero
import Pez
import Reptil
class Animal:
    _totalAnimales=0
    def __init__ (self,nombre, edad,habitat,genero,zona):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal._totalAnimales +=1

    def movimiento(self):
        return "Desplazarse"
    @classmethod
    def total_por_tipo():
        return "Mamíferos: " + str(Mamifero.cantidad_mamiferos()) + "\n" + \
           "Aves: " + str(Ave.cantidad_aves()) + "\n" + \
           "Reptiles: " + str(Reptil.cantidad_reptiles()) + "\n" + \
           "Peces: " + str(Pez.cantidad_peces()) + "\n" + \
           "Anfibios: " + str(Anfibio.cantidad_anfibios())

    def __str__(self):
        if self.zona is not None:
            return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}, la zona en la que me ubico es {}, en el {}".format(self.getNombre(), self.getEdad(), self.getHabitat(), self.getGenero(), self.zona.getNombre(), self.zona.getZoo())
        else:
            return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self.getNombre(), self.getEdad(), self.getHabitat(), self.getGenero())
    
    def toString(self):
        return self.__str__()

    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    def setTotalAnimales(cls,numero):
        cls._totalAnimales=numero

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    
    def get_habitat(self):
        return self._habitat

    def set_habitat(self, habitat):
        self._habitat = habitat

    
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    
    def get_zona(self):
        return self._zona

    def set_zona(self, zona):
        self._zona = zona
