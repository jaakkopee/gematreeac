from gematree_funcs import *

#PROJECT STATUS: broken, I'm thinking..

def getPath(word):
    return listToInt(parentList(getGematria(word)))

class Word:
    def __init__(self, word):
        self.value = getGematria(word)
        self.word = word
        self.path = getPath(word)
        return

    def printSelf(self):
        print(self.word)
        for i in self.path:
            print(i)
        return

words = []

def addWord(word):
    global words
    words += [Word(word)]
    return

def printAll():
    global words
    for i in words:
        print(i.word+" "+str(i.value))
        print (i.path)
    return

def printSelves():
    global words
    for i in words:
        i.printSelf()
    return
    