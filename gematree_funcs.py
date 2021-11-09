from itertools import permutations

alphabet = {"a":2,"b":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":10,"j":20,"k":30,"l":40,"m":50,"n":60,"o":70,"p":80,"q":90,"r":100,"s":200,"t":300,"u":400,"v":500,"w":600,"x":700,"y":800,"z":900,"å":1000,"ä":2000,"ö":3000}


def getGematria(word):
	value=0
	for i in word:
		value+=alphabet[i]
		
	return value
	


def findParent(value):
	vstr=str(value)
	outVal=0
	for i in vstr:
		outVal+=int(i)
		
	return outVal



def parentList(value):
	pList=[str(value)]
	
	while value>9:
		value=findParent(value)
		pList+=[str(value)]
	#pList.reverse()
	return pList



def permutateList(value):
	numList=[x for x in str(value)]
	pList=list(permutations(numList))
	
	outList=[]
	tmpStr=''
	
	for i in pList:
		for j in i:
			tmpStr+=str(j)
		if tmpStr not in outList and tmpStr[0]!='0': outList+=[tmpStr]
		tmpStr=''
	return outList



def permutatedParents(value):
	parList=parentList(value)
	perParList=[]

	for i in parList:
		perParList+=[permutateList(i)]

	return perParList

def listToInt(ppList):
	ppList = [int(i) for i in ppList]		
	return ppList

		
		

