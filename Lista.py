from zope.interface import implementer
from Heladera import Heladera
from IColeccion import IColeccion
from Lavarropa import Lavarropa
from Nodo import Nodo
from Televisor import Televisor
@implementer(IColeccion)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato 
    def insertarElemento(self,elemento,posicion):
        nodo=Nodo(elemento)
        error=False
        if posicion==0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=self.__comienzo
            self.__tope+=1
        else:
            if self.__comienzo==None:
                error=True
            else:
                aux=self.__comienzo
                anterior=self.__comienzo
                i=0
                while aux!=None and i!=posicion:
                    anterior=aux
                    aux=aux.getSiguiente()
                    i+=1
                if aux==None:
                    error=True
                else:
                    anterior.setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    self.__tope+=1
        if error:
            raise IndexError
    def agregarElemento(self,elemento):
        nodo=Nodo(elemento)
        if self.__comienzo==None:
            self.__comienzo=nodo
            self.__actual=self.__comienzo
        else:
            aux=self.__comienzo
            anterior=self.__comienzo
            while aux!=None:
                anterior=aux
                aux=aux.getSiguiente()
            anterior.setSiguiente(nodo)
        self.__tope+=1
    def mostrarElemento(self,posicion):
        error=False
        if self.__comienzo==None:
            error=True
        else:
            i=0
            aux=self.__comienzo
            while aux!=None and i!=posicion: 
                aux=aux.getSiguiente()
                i+=1
            if aux==None:
                error=True
            else:
                tipo=''
                if type(aux.getDato())==Televisor:
                    tipo='Televisor'
                elif type(aux.getDato())==Lavarropa:
                    tipo='Lavarropa'
                elif type(aux.getDato())==Heladera:
                    tipo='Heladera'
                print('El tipo de aparato almacenado en la posicion:{} es:{}'.format(posicion,tipo))
        if error:
            raise IndexError