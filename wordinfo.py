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
    font-size:56px;
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
from gemadbconn import *
from deepmem import *

form = cgi.FieldStorage()
try:
    word = form["word"].value
except:
    word =''

print("</style></head>")
print("<body>")
print ("<a id='hyperlinque' href='/index.html'>Home</a>", end=" ")
print ("<a id='hyperlinque' href='gematreeac.py?word=SHOW'>"+"Session Memory View"+"</a>")

print("<p>Information on word '"+word+"' coming soon...")
print("</body></html>")

con.close()
conDM.close()
