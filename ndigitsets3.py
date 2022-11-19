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

    def getWords(self):
        return self.words

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
        outputWord=""

        for chkWord in words2D:
            if getGematria(chkWord[0], currentCipher) == getGematria(word, currentCipher):
                    
                if chkWord not in self.printed:
                    for i in chkWord:
                        outputWord+=\
                            "<div class='hyperWordDiv' id='hwd_"+str(getGematria(i, currentCipher))+"_"+i+"'>"
                        outputWord+=\
                            "<button class='hyperWordButton' id='hwb_"+i+"'>"+i+"</button>\
                            <div class='hyperWordMenuContent' id='hwmc_"+i+"'>\
                                <a href='#' id='hwDel_"+i+"'>delete</a>\
                            </div>\
                            </div>"

                        
                    self.printed+=[chkWord]
                else:
                    return "printed"

        return outputWord


    def printMe(self, currentCipher):
        retval=""
        retval+=\
            "<div class='Root' id='Root_"+str(self.root)+"'>\
                <p class='rootClass' id='rootP_"+str(self.root)+"'>\
                    Root "+str(self.root)+"</p>"
        #Root-div ends at the end of Root...

        for routeIter in self.routes:
            retval = retval + "<br /><a href='#' class='routeClass' id='route_"+str(routeIter)+"'>"+str(routeIter)+"</a>"
            wordsToBePrintedOnThisRoute=[]
            for word in self.words:
                if getParentList(getGematria(word, currentCipher))[1:]==routeIter:
                    wordsToBePrintedOnThisRoute+=[word]
            
            oldGemVal=0
            for word_idx in range(len(wordsToBePrintedOnThisRoute)):
                gemVal=getGematria(wordsToBePrintedOnThisRoute[word_idx], currentCipher)

                if word_idx>0:
                    oldGemVal=getGematria(wordsToBePrintedOnThisRoute[word_idx-1], currentCipher)
            
                if not gemVal==oldGemVal or word_idx==0:
                    retval+=makeHyperNumber(str(gemVal))
                    
                hyperWord=self.makeHyperWord(wordsToBePrintedOnThisRoute[word_idx], currentCipher)

                if not hyperWord=="printed":
                    retval += hyperWord

        retval+="</div>"
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
    newNumStr=""
    if numStr==0:
        newNumStr+=\
          "<div class='hyperWordDiv' id='hwd_"+numStr+"_"+numStr+"'>\
            <button class='hyperNumberButton' id='hwb_nolla'>"+numStr+"</button>\
            <div class='hyperWordMenuContent' id='hwmc_"+numStr+"'>\
                <a href='#' id='hwWCSearch_"+numStr+"'>Wizard:"+numStr+"</a>\
                <a href='#' id='hwSF_"+numStr+"'>SentForm:"+numStr+"</a>\
            </div>\
          </div>"
    else:
        newNumStr+=\
        "<div class='hyperWordDiv' id='hwd_"+numStr+"_"+numStr+"'>\
            <button class='hyperNumberButton' id='hwb_"+numStr+"'>"+numStr+"</button>\
            <div class='hyperWordMenuContent' id='hwmc_"+numStr+"'>\
                <a href='#' id='hwWCSearch_"+numStr+"'>Wizard:"+numStr+"</a>\
                <a href='#' id='hwSF_"+numStr+"'>SentForm:"+numStr+"</a>\
            </div>\
        </div>"

    return newNumStr

def makeWCHyperWord(word):
    return "<button class='WCWord' id='WC"+word+"' value='"+word+"'>"+word+"</button>"

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
        #outputString+=str(getParentList(getGematria(i[0], currentCipher)))+" "

        for j in i:
            outputString+="<button class='sfString' id='SF"+j+"'>"+j+"</button> "

        outputString+="<br />"

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

def addWordArray(wordArray, currentCipher):
    for i in wordArray:
        addWord(i, currentCipher)
    return
    
def printAll(currentCipher):
    retval=""
    global roots
    
    for i in roots:
        retval = retval + i.printMe(currentCipher)

    return retval

def clearRAM():
    global roots
    del roots
    roots = []


