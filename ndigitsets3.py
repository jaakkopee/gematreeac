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

#THIS NEXT!
def generatePossibleRoutes(route):
    return route

class Root:
    def __init__(self, word):
        chkWord=word
        alphakeys = list(alphabet.keys())
        for i in chkWord:
            if i not in alphakeys:
                word=word.replace(i, "0")

        gemVal = getGematria(word)
        self.root = getRootNumber(gemVal)
        self.words = [word]
        self.routes = [getParentList(gemVal)[1:]]
        return

    def addWord(self, word):
        chkWord=word
        alphakeys = list(alphabet.keys())
        for i in chkWord:
            if i not in alphakeys:
                word=word.replace(i, "0")

        gemVal = getGematria(word)
        route = getParentList(gemVal)[1:]
           
        if self.root == getRootNumber(gemVal):

            if route in self.routes:
                self.words+=[word]
                return True

            self.words+=[word]
            self.routes+=[route]
            return True
            
        return False

    def printMe(self):
        print ("Root "+str(self.root),  end=":\n")
        for i in self.routes:
            print (str(i), end=" / ")
            for j in self.words:
                gemVal = getGematria(j)
                pl = getParentList(gemVal)[1:]
                if  pl == i:
                    print (str(gemVal)+" "+j, end="  ")
            print()
        print()

        return

    def sortWords(self):

        for i in range(1, len(self.words)):
            
            key = self.words[i]

            j= i-1
            while j >= 0 and getGematria(key) < getGematria(self.words[j]):
                self.words[j+1] = self.words[j]
                j-=1
            self.words[j+1] = key
        
        return

roots = []

def sortRoots():
    global roots

    for i in range(1, len(roots)):
            
        key = roots[i]

        j= i-1
        while j >= 0 and key.root < roots[j].root:
            roots[j+1] = roots[j]
            j-=1
        roots[j+1] = key

    return

def sortWordsAndRoots():
    global roots
    
    for i in roots:
        i.sortWords()
    sortRoots()
    
    return


def addWord(word):
    global roots
    
    if len(roots)==0:
        roots+=[Root(word)]
        return

    rootFound=False
    for i in roots:
        rootFound = i.addWord(word)
        if rootFound:
            sortWordsAndRoots()
            return

    if not rootFound:
        roots+=[Root(word)]
        sortWordsAndRoots()
        return

    return


def printAll():
    global roots
    for i in roots:
        i.printMe()
    return

def clearRAM():
    global roots
    del roots
    roots = []

