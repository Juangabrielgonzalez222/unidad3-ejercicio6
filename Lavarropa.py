from AparatoElectronico import AparatoElectronico

class Lavarropa(AparatoElectronico):
    __capacidad=0
    __velocidadCentrifugado=0
    __programas=0
    __tipoCarga=''
    def __init__(self,marca='',modelo='',color='',pais='',precioBase=0,capacidad=0,velocidadCentrifugado=0,programas=0,tipoCarga=''):
        super().__init__(marca,modelo,color,pais,precioBase)
        self.__capacidad=capacidad
        self.__velocidadCentrifugado=velocidadCentrifugado
        self.__programas=programas
        self.__tipoCarga=tipoCarga
    def verificarTipoCarga(self,tipo):
        resultado=False
        if self.__tipoCarga==tipo:
            resultado=True
        return resultado
    def mostrarMarca(self):
        print('La marca del lavarropa es:',self.getMarca())
    def calcularSegunCaracteristicas(self):
        resultado=0
        porcentaje=0
        if self.__capacidad<=5:
            porcentaje=1
        else:
            porcentaje=3
        resultado=(self.getPrecioBase()*porcentaje)/100
        return resultado
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),capacidad=self.__capacidad,velocidadCentrifugado=self.__velocidadCentrifugado,programas=self.__programas,tipoCarga=self.__tipoCarga))
        return d