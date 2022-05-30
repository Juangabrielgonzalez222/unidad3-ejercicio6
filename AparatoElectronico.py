import abc
from abc import ABC
class AparatoElectronico(ABC):
    __marca=''
    __modelo=''
    __color=''
    __pais=''
    __precioBase=0
    def __init__(self,marca='',modelo='',color='',pais='',precioBase=0):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__pais=pais
        self.__precioBase=precioBase
    def getModelo(self):
        return self.__modelo
    def getMarca(self):
        return self.__marca
    def getPrecioBase(self):
        return self.__precioBase
    @abc.abstractclassmethod
    def calcularSegunCaracteristicas():
        pass
    def calcularImporteVenta(self):
        resultado=0
        resultado=self.__precioBase+self.calcularSegunCaracteristicas()
        return resultado
    def verificarMarca(self,marca):
        resultado=False
        if self.__marca==marca:
            resultado=True
        return resultado
    def mostrarDatos(self):
        print('Marca:{} Pais:{} Importe de venta:{}'.format(self.__marca,self.__pais,self.calcularImporteVenta()))
    def toJSON(self):
        return dict(marca=self.__marca,modelo=self.__modelo,color=self.__color,pais=self.__pais,precioBase=self.__precioBase)