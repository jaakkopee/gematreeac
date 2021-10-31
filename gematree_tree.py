from gematree_funcs import *

class gemaNode:
    def __init__(self, word=None, gemValue=0):
        self.word=word
        self.gemValue=gemValue

        if word:
            self.gemValue=getGematria(self.word)
        else:
            self.gemValue=gemValue
            
        self.ppList=ppListToInt(permutatedParents(self.gemValue))
        self.children=[]
            

        for i in self.ppList:
            for j in i:
                child=gemaNode(None, j)
                self.children+=[child]
        return

    def printTree(self):
        for i in self.children:
            print ("word: "+i.word+" value: "+str(i.gemValue))
            i.printTree()

