from ManejadorAparato import ManejadorAparato
from Menu import Menu
from ObjectEncoder import ObjectEncoder

if __name__== '__main__':
	objectEncoder=ObjectEncoder()
	manejadorAparato=None
	archivo='aparatoselectronicos.json'
	diccionario=objectEncoder.leerJSONArchivo('aparatoselectronicos.json')
	if diccionario!=-1:
		manejadorAparato=objectEncoder.decodificarDiccionario(diccionario)
		print('Se cargaron datos del archivo',archivo)
	else:
		manejadorAparato=ManejadorAparato()
	menu=Menu()
	menu.lanzarMenu(manejadorAparato,objectEncoder)