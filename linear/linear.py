import numpy as NP

def loadDataset():
	x = NP.matrix("1 1;1 2;1 3;1 4;1 5;1 6;1 7;1 8") # 8 x 2
	y = NP.matrix("1;2;3;4;5;6;7;8") # 8 x 1
	theta = NP.matrix("0;0") # 2 x 1
	return x,y,theta

def findParameter(num_iter,alpha):
	x,y,theta = loadDataset()
	#j(theta0,theta1) = 1/m(h(x) - y)^2
	#j(theta0,theta1) = theta0+theta1*x
	#h(x) = theta_0 + theta_1 * x
	# 8 x 2  ---  2 x 1 ==> (8 x 2)"==> (2 x 8) ---- (8 x 1)
	
	
	for iter in range(num_iter):
		theta = theta - (0.1/x.shape[0])*(x.T * ((x*theta) - y))
	
	return theta

def testLinear():
	parameter = findParameter(15,0.1)
	print "Los parametros estimados son :",parameter
	