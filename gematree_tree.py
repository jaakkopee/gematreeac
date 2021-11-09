from gematree_funcs import *

class gemaNode:
    def __init__(self, word=None, gemValue=0):
        self.word=word
        self.gemValue=gemValue
        self.parent = None

        if word:
            self.gemValue=getGematria(self.word)
        else:
            self.gemValue=gemValue
            
        self.parentNumbers=listToInt(parentList(self.gemValue))
        if self.gemValue > 9:
            self.parent = gemaNode(word=None, gemValue=findParent(self.gemValue))
             
        return

def printTree(rootNode):
    print (rootNode.word)
    print (rootNode.gemValue)
    if rootNode.gemValue > 0: #0 is true root
        printTree(rootNode.parent)

