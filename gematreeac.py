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
    words = getWordsFromDeepMem()
    print("<div id='perkele2'>")

    for i in range(1, len(words)):
            
        key = words[i]

        j= i-1
        while j >= 0 and getGematria(key[0]) < getGematria(words[j][0]):
            words[j+1] = words[j]
            j-=1
        words[j+1] = key


    for i in words:
        print("<p>"+i[0]+ " "+ str(getGematria(i[0]))+"</p>")
    
    print("</div>")

    con.close()
    conDM.close()
    sys.exit()



if word == "ADDTODEEPMEM":
    words = getWordsFromSQL()
    
    print("<div id='perkele'>")
    
    print("Words to DeepMem:")
    for i in words:
        if addWordToDeepMem(i[0]):
            print ("Added '"+i[0]+"'")
        else:
            print ("Did not add '"+i[0]+"' for it was already in DeepMem")

    print("</div>")

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

    con.close()
    conDM.close()
    sys.exit()

if word == "ALPHABET":
    print("<div id='perkele'>")
    for i in alphabet.items():
        print(i)
    
    print("</div>")
    con.close()
    conDM.close()
    sys.exit()

if word == "CLEAR":
    clearRAM()
    cur.execute("delete from wordpool")
    con.commit()
    con.close()
    conDM.close()
    print("<h1><center>Database Cleared</center></h1>")
    sys.exit()

if word == "SHOW":
    print("<div id='perkele'>")
    printDB()
    print("</div>")
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
print("</div>")

print("</body></html>")