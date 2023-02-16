from NineRootedTreeWords import *
text = open("parisanaa.txt", "r").read()
for char in text:
    if not char.isalnum() and not char.isspace():
        text = text.replace(char, "")

wordList = text.split()
wordList = [i.lower() for i in wordList]
wordList = list(dict.fromkeys(wordList))
wordList = sorted(wordList)
rootChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#wordList.extend(rootChars)

tree = wordList_to_NineRootedTree(wordList, "ScaExt")

print(tree)

for i in tree.roots[1:]:
    if i:
        print (i.words)

print(tree.generateNestedList())
