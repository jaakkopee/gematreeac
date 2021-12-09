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

form = cgi.FieldStorage()
try:
    word = form["word"].value
except:
    word =''

#word=word.replace(" ", "")

if word == "ALPHABET":
    print("<div id='perkele'>")
    for i in alphabet.items():
        print(i)
    
    print("</div>")
    con.close()
    sys.exit()

if word == "CLEAR":
    clearRAM()
    cur.execute("delete from wordpool")
    con.commit()
    con.close()
    print("<h1><center>Database Cleared</center></h1>")
    sys.exit()

if word == "SHOW":
    print("<div id='perkele'>")
    printDB()
    print("</div>")
    con.close()
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
