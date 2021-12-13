#!/usr/bin/python3

import cgi, cgitb, sys
cgitb.enable()

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

print("</style></head>")
print("<body>")


from deepmem import *
from gemadbconn import *

form = cgi.FieldStorage()
try:
    inputVal = form["value"].value
except:
    inputVal =''

if inputVal.isnumeric():
    number = int(inputVal)
    
    print ("<a id='hyperlinque' href='/index.html'>Home</a>", end=" ")
    print ("<a id='hyperlinque' href='gematreeac.py?word=SHOW'>"+"Session Memory View"+"</a>")

    print("<div id='perkele'>")    
    print("Current Session:")
    print("(click word to add into DeepMem)")

    for i in searchNumberFromSQL(number):
        hyperWord="<a href='deepmem_ui.py?value="+i[0]+"'>"+i[0]+"</a>"
        print (hyperWord+" "+str(i[1]))
    print()

    print ("DeepMem:\n(click word to add to session memory)")
    for i in searchDeepMemByNumber(number):
        hyperWord="<a href='gematreeac.py?word="+i[0]+"'>"+i[0]+"</a>"
        print (hyperWord, end=" ")
        print (i[1])
    
    print("</div>")
    print("</body></html>")

    con.close()
    conDM.close()
    sys.exit()

if inputVal.isalpha():

    print ("<a id='hyperlinque' href='/index.html'>Home</a>", end=" ")
    print ("<a id='hyperlinque' href='gematreeac.py?word=SHOW'>"+"Session Memory View"+"</a>")
    print ("<a id='hyperlinque' href='deepmem_ui.py?value="+str(getGematria(inputVal))+"'>"+"Back to search results"+"</a>")
    
    print ("<div id='perkele'>")
    
    print("Words to DeepMem:")
    if addWordToDeepMem(inputVal):
        print ("Added '"+inputVal+"'")
    else:
        print ("Did not add '"+inputVal+"' for it was already in DeepMem")

    print("</div>")
    print("</body></html>")
    con.close()
    conDM.close()
    sys.exit()

print("ERROR")
print("</body></html>")
con.close()
conDM.close()
sys.exit()
