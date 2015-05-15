# -*- coding: utf-8 -*-
import math

def createVocabulary(dataVec):
	vectSet = set([])
	for data in dataVec:
		vectSet = vectSet | set(data)
	return list(vectSet)
	
def word2Vec(vocabulary,inputSet):
	vecFromWord = [0] * len(vocabulary)
	for word in inputSet:
		if word in vocabulary:
			vecFromWord[vocabulary.index(word)] = 1
	return vecFromWord

def train(dataVec,labelVec):
	numDoc = len(dataVec)
	numWords = len(dataVec[0])
	listOfCategories = list(set(labelVec))
	probCategory = []
	for category in listOfCategories:
		probCategory.append(float(labelVec.count(category))/numDoc)
	
	pNum = [[1] * numWords] * len(probCategory)
	pDen = [2.0] * len(probCategory)
	
	for index in range(numDoc):
		labelIndex = labelVec[index]
		for indexWord in range(numWords):
			pNum[labelIndex-1][indexWord] += dataVec[index][indexWord]
			pDen[labelIndex-1] += dataVec[index][indexWord]
	
	probabilitys = []
	for labelIndex in range(len(probCategory)):
		probabilitys.append([])
		for wordIndex in range(numWords):
			probabilitys[labelIndex].append(math.log(pNum[labelIndex][wordIndex]/pDen[labelIndex]))

	return probabilitys, probCategory

def getVecFromText(text):
	import re
	regex = re.compile("[^\u00E0-\u00FC\w]")
	tmpListOfWords = regex.split(text)
	return [word.lower() for word in tmpListOfWords if len(word)>2]

def removeAccent(text):
	text.replace("\xa0","a")
	text.replace("\x82","e")
	text.replace("\xa1","i")
	text.replace("\xa2","o")
	text.replace("\xa3","u")
	text.replace("á","a")
	text.replace("é","e")
	text.replace("í","i")
	text.replace("ó","o")
	text.replace("ú","u")

def classify(inputSet,probabilitys,probabilityCategory):
	numWords = len(probabilitys[0])
	numCategories = len(probabilityCategory)
	finalProbability = [0] * numCategories
	for indexCategory in range(numCategories):
		tmpSum = 0.0
		for indexWord in range(numWords):
			print "TMPSUM : ",tmpSum
			tmpSum += probabilitys[indexCategory][indexWord] * inputSet[indexWord]
			print "TMPSUM : ",tmpSum,"   -- ", inputSet[indexWord]
		print "La suma es : ",tmpSum
		finalProbability[indexCategory] = tmpSum + math.log(probabilityCategory[indexCategory])
		
	categories = ["Ciencia","Deportes","Economia","Salud","Tecnologia"]
	
	print "Pertenece a :", finalProbability.index(max(finalProbability))		
		
	
def testTrain():
	documentos = []
	labelDocumentos = []
	for i in range(1,12):
		documentos.append(getVecFromText(open("data/ciencia/%d.txt"%i).read()))
		labelDocumentos.append(1)
		documentos.append(getVecFromText(open("data/deportes/%d.txt"%i).read()))
		labelDocumentos.append(2)
		documentos.append(getVecFromText(open("data/economia/%d.txt"%i).read()))
		labelDocumentos.append(3)
		documentos.append(getVecFromText(open("data/salud/%d.txt"%i).read()))
		labelDocumentos.append(4)
		documentos.append(getVecFromText(open("data/tecnologia/%d.txt"%i).read()))
		labelDocumentos.append(5)
	vocabulary = createVocabulary(documentos)
	#print vocabulary
	documentoVec = []
	for data in documentos:
		documentoVec.append(word2Vec(vocabulary,data))
	
	probabilitys, probCategory = train(documentoVec,labelDocumentos)

	return probabilitys,probCategory,vocabulary


	