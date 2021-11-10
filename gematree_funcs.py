from itertools import permutations

alphabet = {"0":0, "a":1, "b":2, "c":3, "d":4, "e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"q":80,"r":90,"s":100,"t":200,"u":300,"v":400,"w":500,"x":600,"y":700,"z":800,"å":900,"ä":1000,"ö":2000}


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
	pList.reverse()
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

		
		

