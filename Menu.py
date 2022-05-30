from Heladera import Heladera
from Lavarropa import Lavarropa
from Televisor import Televisor
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7,
            8:self.salir
        }
    def lanzarMenu(self,manejadorAparato,objectEncoder):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para insertar un aparato en la colección en una posición determinada.')
            print('-Ingrese 2 para agregar un aparato a la colección.')
            print('-Ingrese 3 para dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.')
            print('-Ingrese 4 para mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.')
            print('-Ingrese 5 para mostrar la marca de todos los lavarropas que tienen carga superior.')
            print('-Ingrese 6 para mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.')
            print('-Ingrese 7 para Almacenar los objetos de la colección Lista en el archivo.')
            print('-Ingrese 8 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<7:
                ejecutar(manejadorAparato)
            elif opcion==7:
                ejecutar(manejadorAparato,objectEncoder)
            else:
                ejecutar()
    def opcion1(self,manejadorAparato):
        aparato=self.cargarAparato()
        if aparato!=-1:
            posicion=self.cargarNumeroEntero('Ingrese posicion a insertar en la lista:\n')
            manejadorAparato.insertarAparato(aparato,posicion)
    def opcion2(self,manejadorAparato):
        aparato=self.cargarAparato()
        if aparato!=-1:
            manejadorAparato.agregarAparato(aparato)
    def opcion3(self,manejadorAparato):
        posicion=self.cargarNumeroEntero('Ingrese posicion:\n')
        manejadorAparato.mostrarAparato(posicion)
    def opcion4(self,manejadorAparato):
        manejadorAparato.cantidadAparatosMarca()
    def opcion5(self,manejadorAparato):
        manejadorAparato.mostrarLavarropaSuperior()
    def opcion6(self,manejadorAparato):
        manejadorAparato.mostrarDatos()
    def opcion7(self,manejadorAparato,objectEncoder):
        manejadorAparato.guardarArchivo(objectEncoder)
    def cargarAparato(self):
        resultado=-1
        print('A continuación debe seleccionar el aparato: \n1:Televisor,2:Lavarropa,3:Heladera')
        tipo=self.cargarNumeroEntero('Ingrese el numero del tipo de aparato:\n')
        aparato=None
        if tipo>0 and tipo<4:
            marca=input('Ingrese marca:\n')
            modelo=input('Ingrese modelo:\n')
            color=input('Ingrese color:\n')
            pais=input('Ingrese pais:\n')
            precioBase=self.cargarFlotante('Ingrese precio base:\n')
            if tipo==1:
                pantalla=input('Ingrese tipo pantalla:\n')
                pulgadas=self.cargarNumeroEntero('Ingrese cantidad pulgadas:\n')
                definicion=input('Ingrese tipo de definicion:\n')
                conexionInternet=self.cargarBool('Tiene conexion a internet:')
                aparato=Televisor(marca,modelo,color,pais,precioBase,pantalla,pulgadas,definicion,conexionInternet)
            elif tipo==2:
                capacidad=self.cargarNumeroEntero('Ingrese capacidad:\n')
                velocidadCentrifugado=self.cargarNumeroEntero('Ingrese velocidad centrifugado:\n')
                programas=self.cargarNumeroEntero('Ingrese la cantidad de programas\n')
                tipoCarga=input('Ingrese el tipo de carga:\n')
                aparato=Lavarropa(marca,modelo,color,pais,precioBase,capacidad,velocidadCentrifugado,programas,tipoCarga)
            else:
                capacidad=self.cargarNumeroEntero('Ingrese capacidad:\n')
                freezer=self.cargarBool('Tiene freezer:')
                ciclica=self.cargarBool('Es ciclica:')
                aparato=Heladera(marca,modelo,color,pais,precioBase,capacidad,freezer,ciclica)
            resultado=aparato
        else:
            print('El numero ingresado no corresponde a ningun tipo.')  
        return resultado
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se admiten numeros enteros y punto ,por ejemplo:500 o 500.50')
            else:
                bandera=False
        return numero
    def cargarBool(self,mensaje):
        resultado=None
        bandera=True
        opcion=''
        while bandera:
            print(mensaje)
            opcion=input('Ingrese "s" si tiene, "n" en caso contrario.\n')
            if opcion=='s':
                resultado=True
                bandera=False
            elif opcion=='n':
                resultado=False
                bandera=False
            else:
                print('Solo se admite "s" o "n"')
        return resultado
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')