from numpy import *

def loadDataSet():
	data = matrix("1 1 1;1 1 0;1 0 1;1 0 0") # 4 x 3
	label = matrix("1;1;1;-1") # 4 x 1
	return data,label
	
def optimizeParameter():
	dataSet,label = loadDataSet()
	m,n = dataSet.shape
	w = mat(zeros(n)) # 1 x 3 
	alpha = 0.001
	while True:
		errorCount = 0
		index = 0
		for data in dataSet:
			#		 1 x 3 * 3 x 1
			output = data * w.T
			#print "Data :",output," Forma:",output.shape
			output = 1 if output>0 else -1
			error = label[index] - output
			#print "error :",error," Forma:",error.shape
			if(error != 0):
				errorCount+=1
				w = w + alpha * (label[index] * data)
			index+=1
		if(errorCount == 0):
			break
	return w
	
def graphData():
	import matplotlib.pyplot as plt
	dataSet,label = loadDataSet()
	weights = array(optimizeParameter())
	xCoordPos = []
	yCoordPos = []
	xCoordNeg = []
	yCoordNeg = []
	
	for i in range(len(label)):
		if(label[i]==1):
			xCoordPos.append(dataSet[i,1])
			yCoordPos.append(dataSet[i,2])
		else:
			xCoordNeg.append(dataSet[i,1])
			yCoordNeg.append(dataSet[i,2])
			
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xCoordPos, yCoordPos, s=30, c='blue', marker='+')
	ax.scatter(xCoordNeg, yCoordNeg, s=30, c='red',marker='o')	
	
	x = arange(-3.0, 3.0, 0.1)
	y = (-weights[0][0]-weights[0][1]*x)/weights[0][2]
	ax.plot(x, y)
	
	plt.show()
	
'''
def plotBestFit(wei):
	import matplotlib.pyplot as plt
	weights = wei.getA()
	dataMat,labelMat=loadDataSet()
	dataArr = array(dataMat)
	n = shape(dataArr)[0]
	xcord1 = []; ycord1 = []
	xcord2 = []; ycord2 = []
	for i in range(n):
	if int(labelMat[i])== 1:
	xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
	else:
	xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
	ax.scatter(xcord2, ycord2, s=30, c='green')
	x = arange(-3.0, 3.0, 0.1)
	y = (-weights[0]-weights[1]*x)/weights[2]
	ax.plot(x, y)
	plt.xlabel('X1'); plt.ylabel('X2');
	plt.show()


'''
	