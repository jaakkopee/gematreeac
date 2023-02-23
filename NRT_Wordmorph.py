import NineRootedTreeWords as nrt
import getwordsfromdbs as gwdb
import gemNumFuncs as gnf
import nltk
from nltk.tokenize import SyllableTokenizer
import sys
import random
import warnings
        
        
warnings.filterwarnings("ignore")

try:
    inputString = sys.argv[1]
except IndexError:
    print("No input string, cannot operate.")
    sys.exit()

try:   
    transformMode = sys.argv[2]
except IndexError:
    print("Define mode of operation in the command line as 'syllable', or 'word'")
    sys.exit()

if transformMode not in ["syllable", "word"]:
   print("Invalid mode of operation. Should be 'syllable' or 'word'")
   sys.exit()

inputString = inputString.lower()

for i in inputString:
    if not i.isalpha() and not i.isspace():
        inputString = inputString.replace(i, "")

userWordList = inputString.split()

syllableTokenizer = SyllableTokenizer()

def extractSyllables(wordList):
    outArray = []
    for i in wordList:
        outArray += [syllableTokenizer.tokenize(i)]
    return outArray

dbWordList = gwdb.getDeepMem()
dbTreeSyllableList2D = extractSyllables(dbWordList)
dbTreeSyllableList1D = []

for i in dbTreeSyllableList2D:
    for j in i:
        dbTreeSyllableList1D += [j]


wordTree = nrt.NineRootedTree(dbWordList, "ScaExt")
syllableTree = nrt.NineRootedTree(dbTreeSyllableList1D, "ScaExt")


def transformWord(wordList):
    global wordTree
    outList=[]
    outputString = ""

    for i in wordList:
        wordsFromTree = wordTree.findWords(gnf.getGematria(i, "ScaExt"))
        if wordsFromTree == []:
            wordsFromTree = [i]
        outList+=[random.choice(wordsFromTree)]

    for i in outList:
        outputString+=i+" "

    return outputString

def transformSyllables(wordList):
    global syllableTree
    outputString = ""

    userSyllables2D = extractSyllables(wordList)

    for i in userSyllables2D:
        for j in i:
            sylsFromTree = syllableTree.findWords(gnf.getGematria(j, "ScaExt"))
            if sylsFromTree == []:
                sylsFromTree = [j]
            outputString += random.choice(sylsFromTree)
        outputString+=" "

    outputString = outputString[0:-1]

    return outputString



#print(wordTree, syllableTree)

outStr = ""

if transformMode == "word":
    outStr = transformWord(userWordList)    

if transformMode == "syllable":
    outStr = transformSyllables(userWordList)


inGV = 0
outGV = 0
for i in outStr.split():
    outGV+= gnf.getGematria(i, "ScaExt")

for i in userWordList:
    inGV += gnf.getGematria(i, "ScaExt")

print (inputString, str(inGV), outStr, str(outGV))

