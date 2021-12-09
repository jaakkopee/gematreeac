
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
    parList =[value]
    parInt = value
    while parInt > 9:
        parInt = findParent(parInt)
        parList+= [parInt]
    return parList

def permutateInt(value):
    strList = []
    outDict = {}

    for i in str(value):
        strList += [i]

    permList = list(permutations(strList))

    tmpStr = ""
    
    for i in permList:
        tmpStr =""
        for j in i:
            tmpStr += j
        if tmpStr[0] != "0" and int(tmpStr) not in outDict.keys():
            outDict[int(tmpStr)]=[] #{key:[]}

    return outDict


class NumberSet:
    def __init__(self, word):
        self.data = []
        nList = parentList(getGematria(word))

        for i in nList:
            self.data += [permutateInt(i)] #a list of dictionaries with list of words as value

        self.addWord(word)
        return

    def addWord(self, word):
        wordGemValue = getGematria(word)
        for i in self.data:
            if wordGemValue in list(i.keys()):
                #here i should check if word is in db already
                i[wordGemValue]+=[word]

        return

    def printSet(self):
        for i in self.data:
            for j in list(i.keys()):
                print (j, end=" ")
                if i[j] != []:
                    print (i[j], end=" ")
            print()
        print()
        return

class gemaWordMap:
    def __init__(self):
        self.rootNumbers = [0,1,2,3,4,5,6,7,8,9] 
        return

    def printMapping(self):
        for i in self.rootNumbers:
            if type(i)== int:
                print(i)
            else:
                i.printSet()
            print()
        return

    def addWord(self, word):
        ns = NumberSet(word)
        place = list(ns.data[-1].keys())[0]
        if type(self.rootNumbers[place]) == int:
            self.rootNumbers[place] = NumberSet(word)
        else:
            self.rootNumbers[place].addWord(word)

        return

    def clearRAM(self):
        self.rootNumbers = [0,1,2,3,4,5,6,7,8,9]


WORDMAP = gemaWordMap() #singleton object

