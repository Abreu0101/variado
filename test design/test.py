import random

def dataSet():
	disenoGeneral = {1:1,2:2,3:3,4:2}

	elementos = [{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"},{"nombre":"test1"}]
	cantidadElementos = len(elementos)

	listaIndices = [indice for indice in range(cantidadElementos)]
	desingFinal = []

	while cantidadElementos > 0:
		claveRandom = (random.random() * 4) + 1
		valorDisenoGeneral = disenoGeneral[claveRandom]

		resultado = cantidadElementos / float(valorDisenoGeneral)

		valorDisenoGeneral = (resultado>1)?valorDisenoGeneral:cantidadElementos

		tmpList = []
		for i in range(valorDisenoGeneral):
			tmpList.append(listaIndices.pop(i))

		desingFinal.append([((resultado>1)?claveRandom:cantidadElementos) : tmpList])

		cantidadElementos -= valorDisenoGeneral

	print designFinal