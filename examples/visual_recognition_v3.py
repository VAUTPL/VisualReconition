import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import time
from numpy import array


def visual_recognition(foto):
	visual_recognition = VisualRecognitionV3('2016-05-20', api_key='you api key')

	with open(join(dirname(__file__), foto), 'rb') as image_file:
		    data=json.dumps(visual_recognition.classify(images_file=image_file, threshold=0.1,
                                            classifier_ids=['you classifier']), indent=2, sort_keys=True)
	jsonToPython = json.loads(data)
	#print(data)
	datoslista = json.dumps(jsonToPython)
	data1 = json.loads(datoslista)	 
	lista = []
	lista2 = []
	for element in data1["images"][0]["classifiers"][0]["classes"]:
	    lista.append(element["class"])
	    lista.append(element["score"])
	    lista2.append(element["score"])
	print lista   
	print 'el nro mayor es: ', mayor(lista2)
	exit()
#metodo que si el porcetnaje esta dentro del rango para abrir la puerta
def mayor(lista):
    if lista ==[]:
        return("error")
    elif len(lista) == 1:
        return(lista)
    lista_nueva = 0
    while lista != []:
        primero = lista[0]
        if lista_nueva > primero:
            lista_nueva = lista_nueva
        else:
            lista_nueva =primero
        lista = lista[1:]
    return(lista_nueva)

