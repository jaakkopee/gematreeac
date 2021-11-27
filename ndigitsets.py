# -*- coding: utf-8 -*-
from math import pow

alphabet = {"0":0, "a":1, "b":2, "c":3, "d":4, "e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"q":80,"r":90,"s":100,"t":200,"u":300,"v":400,"w":500,"x":600,"y":700,"z":800,"å":900,"ä":1000,"ö":2000}

def getGematria(word):
	number=0
	for i in word:
		number+=alphabet[i]
		
	return number

#NDS = n-digit set
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
def getNWCPFromNDS(number):
    nds = getNDS(len(str(number)))
    outSet = []
    for i in nds:
        if findParent(number) == findParent(i):
            outSet += [i]
    return outSet

class gemPair:
    def __init__(self, word):
        self.word = word
        self.number = getGematria(word)
        return

#NWPC = "Numbers With Common Parents"
class NWCPSet:
    def __init__(self, number):
        
        self.routeToRoot = getParentList(number)[1:]
        if self.routeToRoot==[]:
            self.routeToRoot=[getRootNumber(number)]
        self.rootNumber = getRootNumber(number)
        self.gemPairs = []
        return        

    def addWord(self, word):
        if getGematria(word) in getNWCPFromNDS(getGematria(word)):
            self.gemPairs += [gemPair(word)]
        return

    def printMe(self):
        for i in self.gemPairs:
            print (str(i.number) + ": " + i.word, end=" ")
        print(self.routeToRoot)
        return


NWCPSets = []

def clearRAM():
    global NWCPSets
    NWCPSets =[]
    return

def addWord(word):
    global NWCPSets
    newSet = NWCPSet(getGematria(word))

    if NWCPSets==[]:
        print("<p id='DBG'>ndigitsets: init sets</p>")
        NWCPSets+=[newSet]
        newSet.addWord(word)
        return

    for i in NWCPSets:

        if i.rootNumber == newSet.rootNumber and i.routeToRoot != newSet.routeToRoot:
            print("<p id='DBG'>found different route to root " + str(i.rootNumber)+": "+str(newSet.routeToRoot)+"</p>")
            NWCPSets+=[newSet]
            newSet.addWord(word)
            break

        if i.routeToRoot==newSet.routeToRoot:
            print("<p id='DBG'>found new word for route "+str(i.routeToRoot)+"</p>")
            i.addWord(word)
            break

        allRoots=[]
        for j in NWCPSets:
            allRoots+=[j.rootNumber]

        if newSet.rootNumber not in allRoots:
            NWCPSets+=[newSet]
            newSet.addWord(word)
            print("<p id='DBG'>found new root "+str(newSet.rootNumber)+"</p>")
            break

    return

def printAll():
    global NWCPSets
    for i in NWCPSets:
        i.printMe()
    return
