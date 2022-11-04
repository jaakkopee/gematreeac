from alphabet import getCipher
from math import pow

def getGematria(word, currentCipher):
    number=0
    for i in word:
        number+=getCipher(currentCipher)[i]
		
    return number

def getNDS(nDigits):
    highestNumberInNDS = int("9"*nDigits)
    lowestNumberInNDS = int(pow(10, nDigits-1))
    return range(lowestNumberInNDS, highestNumberInNDS+1)


def findParent(number):
	vstr=str(number)
	outVal=0
	for i in vstr:
		outVal+=int(i)
		
	return outVal

def getParentList(number):
    parList =[number]
    parInt = number
    while parInt > 9:
        parInt = findParent(parInt)
        parList+= [parInt]
    return parList

def getRootNumber(number):
    while number > 9:
        number=findParent(number)
    return number

#NWCP = numbers with common parents
def getNWCPFromNDS(number, ndigitset):
    nds = getNDS(ndigitset)
    outSet = []
    for i in nds:
        if getRootNumber(number) == getRootNumber(i):
            outSet += [i]

    return outSet