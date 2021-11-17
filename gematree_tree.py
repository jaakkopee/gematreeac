from itertools import permutations


#Gematreeac by Jaakko Prättälä 2021. Use as thou wilt.

#PROJECT STATUS: better, still not exactly what i want

#TODO: sort paths by node values;
#do something about combining paths.
#check and save permutations of numbers and other numbers with common parents.
#this affects class NumberNode,
#it needs to be able to hold multiple numbers
#work on this in addWord()

alphabet = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":1, "b":2, "c":3, "d":4, "e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"q":80,"r":90,"s":100,"t":200,"u":300,"v":400,"w":500,"x":600,"y":700,"z":800,"å":900,"ä":1000,"ö":2000}


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
    parList =[]
    parInt = value
    while parInt > 9:
        parInt = findParent(parInt)
        parList+= [parInt]
    return parList


def permutateInt(value):
    strList = []
    outList = []

    for i in str(value):
        strList += [i]

    permutations_object = permutations(strList)
    permList = list(permutations_object)
    tmpStr = ""
    for i in permList:
        tmpStr =""
        for j in i:
            tmpStr += j
        if tmpStr[0] != "0" and int(tmpStr) != value and int(tmpStr) not in outList:
            outList += [int(tmpStr)]

    return outList


#Database
words = [] #word-value pairs
paths = [] #numerological relations

#Numerological relations are stored as paths from leave to root of a number, for example [156, 12, 3])

#a tree structure for numerological relations.
class NumberNode:
    def __init__(self, number):
        self.parent = None
        self.value = number
        
        self.neighbors = []

        if len(str(number))>1:                       
            for i in permutateInt(self.value):
                self.neighbors += [(i,)]

            self.parent = NumberNode(findParent(number))

        return

    def printSelf(self):
        global words
        print (" "*len(str(self.value))+str(self.value))
        for i in words:
            if i[1] == self.value:
                print (" "*len(str(self.value))+i[0]+" "+str(self.neighbors))            
        if self.parent:
            self.parent.printSelf()
        return

#Add word to database
#work on this!
def addWord(word):
    global words, paths
    gemValue = getGematria(word)
    if (word, gemValue) not in words:
        words += [(word, gemValue)]

    inPaths = False
    for i in paths: 
        par = i
        while par:
            if par.value == gemValue:
                inPaths = True  
            par = par.parent

    if not inPaths: 
        paths += [NumberNode(gemValue)] #change this!


    return

#Print database
def printAll():
    global words, paths
    for i in paths:
        i.printSelf()                
    return

#Clear database
def clearDB():
    global words,paths
    words = []
    paths = []
    return

def getDB():
    global words, paths
    return [words, paths]
