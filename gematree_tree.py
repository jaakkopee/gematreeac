from gematree_funcs import *

#PROJECT STATUS: better, still not exactly what i want
#TODO: sort paths by 1-digit numbered nodes; do something about combining paths, no duplicates

words = []
paths = []


class NumberNode:
    def __init__(self, number):
        self.parent = None
        self.value = number
        if len(str(number))>1:
            self.parent = NumberNode(findParent(number))

    def printSelf(self):
        global words
        print (" "*len(str(self.value))+str(self.value))
        for i in words:
            if i[1] == self.value:
                print (" "*len(str(self.value))+i[0])
        if self.parent:
            self.parent.printSelf()
        return

def addWord(word):
    global words, paths
    gemValue = getGematria(word)
    words += [(word, gemValue)]
    inPaths = False
    for i in paths: 
        par = i
        while par:
            if par.value == gemValue:
                inPaths = True
            par = par.parent
    if not inPaths: #here TODO: add values to old nodes if they exist
        paths += [NumberNode(gemValue)] #always creates new path

def printAll():
    global words, paths
    for i in paths:
        i.printSelf()                
    
