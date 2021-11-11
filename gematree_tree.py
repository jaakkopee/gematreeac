from gematree_funcs import *

#PROJECT STATUS: broken, I'm thinking..

def getPath(number):
    return listToInt(parentList(number))

class NumberNode:
    def __init__(self, number):
        self.parent = None
        self.children = []
        self.value = number
        if len(str(number))>1:
            self.parent = NumberNode(getPath(number)[len(str(number))-1])

    def printSelf(self):
        print (" "*len(str(self.value))+str(self.value))
        if self.parent:
            self.parent.printSelf()
