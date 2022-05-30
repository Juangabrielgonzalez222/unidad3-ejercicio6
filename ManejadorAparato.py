from AparatoElectronico import AparatoElectronico
from Lavarropa import Lavarropa
from Lista import Lista
class ManejadorAparato:
    __lista=None
    def __init__(self):
        self.__lista=Lista()
    def insertarAparato(self,aparato,posicion):
        if isinstance(aparato,AparatoElectronico):
            try:
                self.__lista.insertarElemento(aparato,posicion)
            except IndexError:
                print('La posicion ingresada no es correcta.')
            else:
                print('Se inserto correctamente el aparato')
        else:
            print('No se pudo añadir un aparato a la lista, tipo de dato incorrecto.')
    def agregarAparato(self,aparato):
        if isinstance(aparato,AparatoElectronico):
            self.__lista.agregarElemento(aparato)
        else:
            print('No se pudo añadir un aparato a la lista, tipo de dato incorrecto.')
    def mostrarAparato(self,posicion):
        try:
            self.__lista.mostrarElemento(posicion)
        except IndexError:
            print('La posicion ingresada no coincide con ningun aparato en la lista.')
    def cantidadAparatosMarca(self):
        cantidad=0
        for aparato in self.__lista:
            if aparato.verificarMarca('philips'):
                cantidad+=1
        print('La cantidad de aparatos philips es:',cantidad)
    def mostrarLavarropaSuperior(self):
        for aparato in self.__lista:
            if type(aparato)==Lavarropa and aparato.verificarTipoCarga('Superior'):
                aparato.mostrarMarca()
    def mostrarDatos(self):
        for aparato in self.__lista:
            aparato.mostrarDatos()
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            aparatos=[aparato.toJSON() for aparato in self.__lista]
        )
        return d
    def guardarArchivo(self,objectEncoder):
        diccionario=self.toJSON()
        objectEncoder.guardarJSONArchivo(diccionario,'aparatoselectronicos.json')