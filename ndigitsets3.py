from math import pow
from gemNumFuncs import *
from alphabet import getCipher

class Root:
    def __init__(self, word, currentCipher):
        chkWord=word
        alphakeys = list(getCipher(currentCipher).keys())
        for i in chkWord:
            if i not in alphakeys:
                word=word.replace(i, "0")

        gemVal = getGematria(word, currentCipher)
        self.root = getRootNumber(gemVal)
        self.words = [word]
        self.routes = [getParentList(gemVal)[1:]]
        self.printed=[]
        return

    def addWord(self, word, currentCipher):

        gemVal = getGematria(word, currentCipher)
        route = getParentList(gemVal)[1:]
           
        if self.root == getRootNumber(gemVal):

            if route in self.routes:
                self.words+=[word]
                return True

            self.words+=[word]
            self.routes+=[route]
            return True
            
        return False

    def makeHyperWord(self, word, currentCipher):
        words2D=make2DWordArray(self.words, currentCipher)
        outputWord="<button class='input' id='words"+str(getGematria(word, currentCipher))+"'>"

        for chkWord in words2D:
            if getGematria(chkWord[0], currentCipher) == getGematria(word, currentCipher):
                if chkWord not in self.printed:
                    outputWord+=str(chkWord)
                    self.printed+=[chkWord]
                else:
                    outputWord+="</button>"
                    return "printed"

        outputWord+="</button>"
        return outputWord


    def printMe(self, currentCipher):
        retval = "\nRoot "+str(self.root) + "\n"

        for i in self.routes:
            retval = retval + str(i)

            for j in self.words:
                gemVal = getGematria(j, currentCipher)
                pl = getParentList(gemVal)[1:]
                if  pl == i:
                    hyperGemValue=makeHyperNumber(str(gemVal))
                    hyperWord=self.makeHyperWord(j, currentCipher)
                    if not hyperWord=="printed":
                        retval = retval + " "+hyperGemValue+" "+hyperWord+" "
            
            
            retval +="\n"
        return retval

    def sortWords(self, currentCipher):

        for i in range(1, len(self.words)):
            
            key = self.words[i]

            j= i-1
            while j >= 0 and getGematria(key, currentCipher) < getGematria(self.words[j], currentCipher):
                self.words[j+1] = self.words[j]
                j-=1
            self.words[j+1] = key
        
        return


def makeHyperNumber(numStr):
    newNumStr="<button class='input' id='number"+numStr+"' value='"+numStr+"'>"+numStr+"</button>"
    return newNumStr

def makeWCHyperWord(word):
    return "<button class='input' id='WC"+word+"' value='"+word+"'>"+word+"</button>"

#                      1        2           3               4           5           6       7
def makeHyperFormula(formula, wordListStr, currentCipher):
    wordArray2D=make2DWordArrayFromString(wordListStr, currentCipher)
    formulaList=formula.split()
    formulaOutArray=[]

    for i in formulaList:
        for j in wordArray2D:
            if getGematria(j[0], currentCipher) == int(i):
                formulaOutArray+=[j]

    outputString=""
    for i in formulaOutArray:
        outputString+=str(getParentList(getGematria(i[0], currentCipher)))+" "
        for j in i:
            outputString+="<button id='SF"+j+"'>"+j+"</button> "
        outputString+="\n"

    return outputString

def make2DWordArrayFromString(wordString, currentCipher):
    wordArrayFlat=wordString.split()
    wordArray=[]
    for i in wordArrayFlat:
        tmpArray=[]

        for j in wordArrayFlat:
            
            if getGematria(i, currentCipher) == getGematria(j, currentCipher):
                tmpArray+=[j]
                tmpArray = list(dict.fromkeys(tmpArray))

        if tmpArray not in wordArray:
            wordArray+=[tmpArray]

    return wordArray

def make2DWordArray(InWordArray, currentCipher):
    wordArrayFlat=InWordArray
    wordArray=[]
    for i in wordArrayFlat:
        tmpArray=[]

        for j in wordArrayFlat:
            
            if getGematria(i, currentCipher) == getGematria(j, currentCipher):
                tmpArray+=[j]
                tmpArray = list(dict.fromkeys(tmpArray))

        if tmpArray not in wordArray:
            wordArray+=[tmpArray]

    return wordArray


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

def sortWordsAndRoots(currentCipher):
    global roots
    
    for i in roots:
        i.sortWords(currentCipher)
    sortRoots()
    
    return


def addWord(word, currentCipher):
    global roots

    if len(roots)==0:
        roots+=[Root(word, currentCipher)]
        return

    rootFound=False
    for i in roots:
        rootFound = i.addWord(word, currentCipher)
        if rootFound:
            sortWordsAndRoots(currentCipher)
            return

    if not rootFound:
        roots+=[Root(word, currentCipher)]
        sortWordsAndRoots(currentCipher)
        return

    return


def printAll(currentCipher):
    retval=""
    global roots
    for i in roots:
        retval = retval + i.printMe(currentCipher)
    retval = retval + '\n'
    return retval

def clearRAM():
    global roots
    del roots
    roots = []


