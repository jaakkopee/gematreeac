from gematree_funcs import *

#PROJECT STATUS: broken, I'm thinking..

class NumberNode:
    def __init__(self, number):
        global paths
        self.parent = None
        self.value = number
        if len(str(number))>1:
            self.parent = NumberNode(findParent(number))

    def printSelf(self):
        print (" "*len(str(self.value))+str(self.value))
        if self.parent:
            self.parent.printSelf()


words = []
paths = []

def addWord(word):
    global words, paths
    gemValue = getGematria(word)
    words += [(word, gemValue)]
    inPaths = False
    for i in paths:
        if i.value == gemValue:
            inPaths = True
    if not inPaths:
        paths += [NumberNode(gemValue)]

def printAll():
    global words, paths
    for i in paths:
        i.printSelf()
        for j in words:
            if j[1] == i.value:
                print (j[0])
    
