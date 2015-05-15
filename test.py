import random

def dataSet():
	disenoGeneral = {1:1,2:2,3:3,4:2}

	elementos = [{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"}]
	cantidadElementos = len(elementos)

	listaIndices = [indice for indice in range(cantidadElementos)]
	desingFinal = []

	while cantidadElementos > 0:
		#print "Generar un random :\n"
		claveRandom = int((random.random() * 4) + 1)
		#print "Random Generado %d"%claveRandom
		valorDisenoGeneral = disenoGeneral[claveRandom]
		#print "Cantidad de elemntos en este diseno : %d\n"%valorDisenoGeneral

		#print "Cantidad de Elementos de momento : %d\n" % cantidadElementos

		resultado = cantidadElementos / float(valorDisenoGeneral)
		#print "El resultado es igual a %f\n"%resultado

		valorDisenoGeneral = valorDisenoGeneral if (resultado>1) else cantidadElementos

		tmpList = []
		for i in range(valorDisenoGeneral-1,-1,-1):
			#print "Indice : %d\n" % i
			tmpList.append(listaIndices.pop(i))
		tmpList.reverse()
		desingFinal.append({(claveRandom if (resultado>1) else cantidadElementos) : tmpList})

		cantidadElementos -= valorDisenoGeneral

		#print "Cantidad de Elementos restantes : %d\n" % cantidadElementos
		#print "=====================================\n"

	print desingFinal