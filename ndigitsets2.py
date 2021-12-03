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

class Root:
    def __init__(self, word):
        gemVal = getGematria(word)
        self.root = getRootNumber(gemVal)
        self.words = [word]
        self.routes = [getParentList(gemVal)[1:]]
        return

    def addWord(self, word):
        gemVal = getGematria(word)
        route = getParentList(gemVal)[1:]
           
        if self.root == getRootNumber(gemVal):

            if route in self.routes:
                self.words+=[word]
                return True


            #Next is not enough. Welcome the concept of possible routes in next block
            #This works fine except with routes [14, 5] and [23, 5]
            foundRouteSubSet=False
            for i in self.routes:
                #       route is a subset               i is a subset
                if (all(x in i for x in route)) ^ (all(x in route for x in i)):
                    foundRouteSubSet=True
            if foundRouteSubSet:
                self.words+=[word]
                self.routes+=[route]                    
                return True

            possibleRoutes=[]
            

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


roots = []

def addWord(word):
    global roots
    
    if len(roots)==0:
        roots+=[Root(word)]
        return

    rootFound=False
    for i in roots:
        rootFound = i.addWord(word)
        if rootFound:
            return

    if not rootFound:
        roots+=[Root(word)]
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

