probabilityExact = 0.8
probabilityOverShoot = 0.1
probabilityUnderShoot = 0.1

def move(p,U):
	n = len(p)
	tmpList = list(p)
	for moveTo in U:
		q = [tmpList[(-moveTo+i)%n] for i in range(n)]
		tmpList = list(q)
	print q
	
def moveToPosition(p,U):
	n = len(p)
	q = [p[(-moveTo+i)%n] for i in range(n)]	
	return q
	
def moveToApplyInnacuracy(p,moveTo):
	n = len(p)
	q = [p[(-moveTo+i)%n] for i in range(n)]	
	
	tmpList = [0.0 for _ in range(n)]
	for index in range(n):
		if q[index] > 0:
			tmpList[index] += q[index] * 0.8
			tmpList[(index-1)%n] += q[index] * 0.1
			tmpList[(index+1)%n] += q[index] * 0.1
	q = list(tmpList)
	return q
			
	