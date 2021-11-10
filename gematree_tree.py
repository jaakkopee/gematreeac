from gematree_funcs import *

#THIS CODE IS BROKEN!
#I'm thinking..

class GemaPath:

    def __init__(self, word):
        self.path = listToInt(parentList(getGematria(word)))
        return


class GemaWord:

    def __init__(self, word):
        self.gemaPath = GemaPath(word)
        self.word = word
        return

    def printSelf(self):
        print (self.gemaPath.path)
        print (self.word)


rootset = [GemaWord("0"), GemaWord("a"), GemaWord("b"), GemaWord("c"), GemaWord("d"), GemaWord("e"), GemaWord("f"), GemaWord("g"), GemaWord("h"), GemaWord("i")]

for i in rootset:
    i.printSelf()


def insertWord(word):
    return






#might need this...
"""
def printTree(rootNode):
    print (rootNode.word)
    print (rootNode.gemValue)
    if rootNode.gemValue > 0: #0 is true root
        printTree(rootNode.parent)

"""