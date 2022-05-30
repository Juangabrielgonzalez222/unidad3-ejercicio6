from AparatoElectronico import AparatoElectronico
class Heladera(AparatoElectronico):
    __capacidad=0
    __freezer=False
    __ciclica=False
    def __init__(self,marca='',modelo='',color='',pais='',precioBase=0,capacidad=0,freezer=False,ciclica=False):
        super().__init__(marca,modelo,color,pais,precioBase)
        self.__capacidad=capacidad
        self.__freezer=freezer
        self.__ciclica=ciclica
    def calcularSegunCaracteristicas(self):
        resultado=0
        porcentaje=0
        if self.__freezer:
            porcentaje+=5
        else:
            porcentaje+=1
        if self.__ciclica:
            porcentaje+=10
        resultado=(self.getPrecioBase()*porcentaje)/100
        return resultado
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),capacidad=self.__capacidad,freezer=self.__freezer,ciclica=self.__ciclica))
        return d