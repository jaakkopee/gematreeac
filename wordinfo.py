#!/usr/bin/python3

import cgi, cgitb
cgitb.enable()
from math import pow
from itertools import permutations
from getwordsfromdbs import searchDeepMemByNumber, getWordsFromSQLByNumber

alphabet = {"0":0, "a":1, "b":2, "c":3, "d":4, "e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"q":80,"r":90,"s":100,"t":200,"u":300,"v":400,"w":500,"x":600,"y":700,"z":800,"å":900,"ä":1000,"ö":2000}

def permutateString(stringToPremutate):
    strList = []
    outList = []

    for i in stringToPremutate:
        strList += [i]

    permList = list(permutations(strList))
    tmpStr = ""
    for i in permList:
        tmpStr =""
        for j in i:
            tmpStr += j
        if tmpStr not in outList:
            outList += [tmpStr]

    return outList


def getGematria(word):
    number=0
    for i in word:
        number+=alphabet[i]
		
    return number

#NDS = n-digit set
def getNDS(nDigits):
    highestNumberInNDS = int("9"*nDigits)
    lowestNumberInNDS = int(pow(10, nDigits-1))
    return range(lowestNumberInNDS, highestNumberInNDS+1)

def findParent(number):
	vstr=str(number)
	outVal=0
	for i in vstr:
		outVal+=int(i)
		
	return outVal

def getParentList(number):
    parList =[number]
    parInt = number
    while parInt > 9:
        parInt = findParent(parInt)
        parList+= [parInt]
    return parList

def getRootNumber(number):
    while number > 9:
        number=findParent(number)
    return number

#NWCP = numbers with common parents
def getNWCPFromNDS(number, ndigitset):
    nds = getNDS(ndigitset)
    outSet = []
    for i in nds:
        if getRootNumber(number) == getRootNumber(i):
            outSet += [i]

    return outSet


print("Content-Type: text/html\n\n")    # HTML is following
print()                                 # blank line, end of headers

print("<html><head>")
print("<meta charset='utf-8'>")
print("<style>")

stylestr = """
#hyperlinque{
    background-color:#aa0055;
    color:#ffffff;
    font-size:40px;
}
#perkele {
    background-color:#ffaacc;
    color:#0044ff;
    font-family:courier;
    font-size:20px;
    white-space:pre;
}
#perkele2 {
    background-color:#ffaacc;
    color:#0044ff;
    font-family:times;
    font-size:20px;
}

#DBG {
    background-color:#00008c;
    color:#ffffff;
    font-size:18px;
    font-family:courier;
    white-space:pre;
}
"""

print(stylestr)

form = cgi.FieldStorage()
try:
    word = form["word"].value
except:
    word =''

print("</style></head>")
print("<body>")
print ("<a id='hyperlinque' href='/index.html'>Home</a>", end=" ")
print ("<a id='hyperlinque' href='gematreeac.py?word=SHOW'>"+"Session Memory View"+"</a>")

print("<div id='perkele2'>")
print("<p>Information on word '"+word+"':</p>")

print ("<h3>Gematria value: "+str(getGematria(word))+"</h3>")

print ("<h3>Anagrams, click on word to add to Session Memory.</h3>")
if len (word) < 8:
    laskuri = 0
    print("<p>")
    for i in permutateString(word):
        laskuri+=1
        print ("<a href='gematreeac.py?word="+i+"'>"+i+"</a>", end = " ")
        if laskuri > 6:
            laskuri = 0
            print("</p><p>")
else: print("Too long a word for anagram printout. Only words shorter than 8 letters are processed.")

print()
print("<h3>Same-rooted numbers in N-Digit-Sets 1,...,4:</h3>")

print( "<p>CLick on SM-words to add them to DeepMem.\
     Click on DM-words to add them to Session Memory.\
    Click on numbers to search session memory and DeepMem</p>")

print("<p>")
for i in range(1, 5):
    print()
    laskuri=0
    print ("<h3>N-Digit-Set: "+str(i)+"</h3>")
    for j in getNWCPFromNDS(getGematria(word), i):
        print ("<a href='gematreeac.py?word="+str(j)+"'>"+str(j)+"</a>", end= " ")
        
        print("{", end=" ")
        print ("SM:", end=" ")
        for k in getWordsFromSQLByNumber(j):
            print("<a href='deepmem_ui.py?value="+k+"'>"+k+"</a>", end=" ")

        print ("DM:", end=" ")
        for k in searchDeepMemByNumber(j):
            print("<a href='gematreeac.py?word="+k[0]+"'>"+k[0]+"</a>", end=" ")

        print("}", end=" ")

        laskuri += 1
        if laskuri > 6:
            laskuri=0
            print("</p><p>")
    print()



print("</div>")

print("</body></html>")
