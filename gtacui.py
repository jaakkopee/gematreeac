from gematree_tree import *

import sqlite3
con = sqlite3.connect("gematreeac.db")
cur = con.cursor()

cur.execute("create table if not exists wordpool (word text)")
con.commit()

def getWordsFromSQL():
    global con, cur
    cur.execute("select * from wordpool")
    data = cur.fetchall()
    return data


def insertWord(word):
    global con, cur
    
    clearDB() #empty RAM

    #load db to RAM
    wordpool = getWordsFromSQL()
    wordpool += [(word,)]
    
    #build tree
    for i in wordpool:
        addWord(i[0])
    
    cur.execute("insert into wordpool values (:wordstr) ", {"wordstr": word})
    con.commit()

    printAll()

    return

