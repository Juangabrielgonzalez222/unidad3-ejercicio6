from AparatoElectronico import AparatoElectronico
class Televisor(AparatoElectronico):
    __pantalla=''
    __pulgadas=0
    __definicion=''
    __conexionInternet=False
    def __init__(self,marca='',modelo='',color='',pais='',precioBase=0,pantalla='',pulgadas=0,definicion='',conexionInternet=False):
        super().__init__(marca,modelo,color,pais,precioBase)
        self.__pantalla=pantalla
        self.__pulgadas=pulgadas
        self.__definicion=definicion
        self.__conexionInternet=conexionInternet
    def calcularSegunCaracteristicas(self):
        resultado=0
        porcentaje=0
        if self.__definicion=='SD':
            porcentaje+=1
        elif self.__definicion=='HD':
            porcentaje+=2
        elif self.__definicion=='FULL HD':
            porcentaje+=3
        if self.__conexionInternet:
            porcentaje+=10
        resultado=(self.getPrecioBase()*porcentaje)/100
        return resultado
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),pantalla=self.__pantalla,pulgadas=self.__pulgadas,definicion=self.__definicion,conexionInternet=self.__conexionInternet))
        return d