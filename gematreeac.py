#!/usr/bin/python3

import cgi, cgitb, sys
cgitb.enable()

print("Content-Type: text/html\n\n")    # HTML is following
print()                                 # blank line, end of headers

print("<html><head>")

print("<meta charset='utf-8'>")
print("<style>")

stylestr = """
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

print("</style></head>")
print("<body>")
from gemadbconn import *
from deepmem import *

form = cgi.FieldStorage()
try:
    word = form["word"].value
except:
    word =''

#word=word.replace(" ", "")

if word == "SHOWDEEPMEM":
    wordsDM = getWordsFromDeepMem()
    print("<div id='perkele2'>")

    for i in range(1, len(wordsDM)):
            
        key = wordsDM[i]

        j= i-1
        while j >= 0 and getGematria(key[0]) < getGematria(wordsDM[j][0]):
            wordsDM[j+1] = wordsDM[j]
            j-=1
        wordsDM[j+1] = key


    for i in wordsDM:
        print("<p>"+i[0]+ " "+ str(getGematria(i[0]))+"</p>")
    
    print("</div>")
    print("</body></html>")

    con.close()
    conDM.close()
    sys.exit()



if word == "ADDTODEEPMEM":
    wordsDM2 = getWordsFromSQL()
    
    print("<div id='perkele'>")
    
    print("Words to DeepMem:")
    for i in wordsDM2:
        if addWordToDeepMem(i[0]):
            print ("Added '"+i[0]+"'")
        else:
            print ("Did not add '"+i[0]+"' for it was already in DeepMem")

    print("</div>")
    print("</body></html>")
    con.close()
    conDM.close()
    sys.exit()

if word.isnumeric():
    number = int(word)
    print("<div id='perkele'>")    
    print("Current Session:")
    for i in searchNumberFromSQL(number):
        print (i[0]+" "+str(i[1]))
    
    print()

    print ("DeepMem:")
    for i in searchDeepMemByNumber(number):
        print (i[0]+" "+str(i[1]))
    
    print("</div>")
    print("</body></html>")

    con.close()
    conDM.close()
    sys.exit()

if word == "ALPHABET":
    print("<div id='perkele'>")
    for i in alphabet.items():
        print(i)
    
    print("</div>")
    print("</body></html>")
    con.close()
    conDM.close()
    sys.exit()

if word == "CLEAR":
    clearRAM()
    cur.execute("delete from wordpool")
    con.commit()
    con.close()
    conDM.close()
    print("<div id='perkele'>")
    print("<h1><center>Erased Session Memory</center></h1>")
    print("</div>")
    print("</body></html>")
    sys.exit()

if word == "SHOW":
    print("<div id='perkele'>")
    printDB()
    print("</div>")
    print("</body></html>")
    con.close()
    conDM.close()
    sys.exit()
    
print("<div id='perkele'>")

#if word and word.islower() and word.isalpha():
#    insertWord(word)
#else:
#    print("invalid string entered")

word=word.lower()
tmpStr = word
for i in tmpStr:
    if not i.isalpha() and not i==" ":
        word=word.replace(i,"")

wordlist=[word][0].split()
for i in wordlist:
    insertWord(i)

printDB()

con.close()
conDM.close()
print("</div>")

print("</body></html>")
