from gematree_funcs import *

#PROJECT STATUS: broken, I'm thinking..

def getPath(word):
    return listToInt(parentList(getGematria(word)))

wordsnpaths = []

def addWord(word):
    global wordsnpaths
    path = getPath(word)
    wordsnpaths += [[word, path]]

def printTree():
    print(wordsnpaths)
    return

