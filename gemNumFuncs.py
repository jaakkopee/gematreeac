from alphabet import getCipher
from math import pow, fabs

def printDistanceData(word1, word2, currentCipher, closenessWeight = 1.0):
    number01 = getGematria(word1, currentCipher)
    number02 = getGematria(word2, currentCipher)
    route01 = getParentList(number01)
    route02 = getParentList(number02)

    distance = getDistance(word1, word2, currentCipher, closenessWeight)

    print(str(number01) + " " + str(route01[1:]))
    print(str(number02) + " " + str(route02[1:]))
    print(distance)

    return

class DistanceTeddyBear:
    def __init__(self, wordList):
        self.wordList = wordList
        self.pointBias = 0.01
        self.commonNds = 0.01
        self.commonRoot = 0.02
        self.commonRoute = 0.08
        self.commonNumber = 0.16
        self.sameWord = 0.061
        self.closenessWeight = 0.01
        self.numberDistanceWeight = 0.06
        self.rootDistanceWeight=0.6
        self.maxDistance = 0.666

        return

    def __str__(self):
        selfString=""
        selfString+="Point Bias: "+str(self.pointBias)+" parameter pointBias\n"
        selfString+="Points from having a common nds: "+str(self.commonNds)+" parameter commonNds\n"
        selfString+="Points from having a common root: "+str(self.commonRoot)+" parameter commonRoot\n"
        selfString+="Points from having a common route: "+str(self.commonRoute)+" parameter commonRoute\n"
        selfString+="Points from having a common number: "+str(self.commonNumber)+" parameter commonNumber\n"
        selfString+="Points from being the same word: "+str(self.sameWord)+" parameter sameWord\n"
        selfString+="Weight on points (how much points matter): "+str(self.closenessWeight)+" parameter closenessWeight\n"
        selfString+="Weight on distance measure of numbers: "+str(self.numberDistanceWeight)+" parameter numberDistanceWeight\n"
        selfString+="Weight on distance measure of roots: "+str(self.rootDistanceWeight)+" parameter rootDistanceWeight\n"
        selfString+="Maximum distance threshold: "+str(self.maxDistance)+" parameter maxDistance\n\n"

        selfString+="""\
            The distance is calculated with:
                totalPoints = closenessWeight*(commonNds + commonRoot + commonRoute + commonNumber + sameWord + pointBias)
                numberDistance = numberDistanceWeight*(abs(gematria(word1) - gematria(word2))
                rootDistance = rootDistanceWeight*(abs(root(word1) - root(word2)))

                distance = numberDistance + rootDistance / totalPoints

        """
        return selfString

    def getDistance(self, word1, word2, currentCipher):
        number01 = getGematria(word1, currentCipher)
        number02 = getGematria(word2, currentCipher)
        root01 = getRootNumber(number01)
        root02 = getRootNumber(number02)
        route01 = getParentList(number01)
        route02 = getParentList(number02)
        points = self.pointBias #an inverse measure of distance (the more the points, the closer the words are)

        #common n digit set
        if len(str(number01)) == len(str(number02)):
            points+=self.commonNds

        #common root
        if root01 == root02:
            points+=self.commonRoot

        #common route
        if route01 == route02:
            points+=self.commonRoute

        #common number
        if number01 == number02:
            points+=self.commonNumber

        #same word
        if word1 == word2:
            points+=self.sameWord

        #a measure of distance (of gematria values). higher numberDistance means farther away
        numberDistance = self.numberDistanceWeight*(fabs(float(number01) - float(number02)))

        #a measure of distance (of roots). higher is farther away
        rootDistance = self.rootDistanceWeight*(fabs(float(root01) - float(root02)))

        totalDistance = rootDistance+numberDistance /  points * self.closenessWeight

        return totalDistance

    def getRestrictedWordSet(self, word, currentCipher):
        
        outputArray=[]
        for i in self.wordList:
            distance = self.getDistance(word, i, currentCipher)
            if distance < self.maxDistance:
                outputArray+=[(i, getGematria(i, currentCipher))]

        return outputArray

    def getGemValsAndDistancesInRWS(self, word, currentCipher):
        rws = self.getRestrictedWordSet(word, currentCipher)
        gwdArray=[]
        chkUniqueArray=[]
        uniqueGemvals = getUniqueGematriaValuesInWVTupleList(rws)
        for i in rws:
            for j in uniqueGemvals:
                if i[1] == j:
                    if j not in chkUniqueArray:
                        chkUniqueArray+=[j]
                        gwdArray+=[(j, self.getDistance(i[0], word, currentCipher))]
        
        return gwdArray


def getUniqueGematriaValuesInWVTupleList(wordList):
    outList = []
    for i in wordList:
        gemval = i[1]
        if gemval not in outList:
            outList+=[gemval]
    return outList

def getDistance(word1, word2, currentCipher, closenessWeight = 1.0):
    number01 = getGematria(word1, currentCipher)
    number02 = getGematria(word2, currentCipher)
    root01 = getRootNumber(number01)
    root02 = getRootNumber(number02)
    route01 = getParentList(number01)
    route02 = getParentList(number02)
    points = 0.01 #an inverse measure of distance (the more the points, the closer the words are)

    #common n digit set
    if len(str(number01)) == len(str(number02)):
        points+=0.01

    #common root
    if root01 == root02:
        points+=0.02

    #common route
    if route01 == route02:
        points+=0.08

    #common number
    if number01 == number02:
        points+=0.16

    #same word
    if word1 == word2:
        points+=0.061

    #a measure of distance (of gematria values). higher numberDistance means farther away
    numberDistance = 0.06*(fabs(float(number01) - float(number02)))

    #a measure of distance (of roots). higher is farther away
    rootDistance = 0.6*(fabs(float(root01) - float(root02)))

    totalDistance = rootDistance+numberDistance /  points * closenessWeight

    return totalDistance
      
def getGematria(word, currentCipher):
    number=0
    cipherInUse=getCipher(currentCipher)
    for i in word:
        number+=cipherInUse[i]
		
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