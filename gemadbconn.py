from gt2 import *
import sqlite3
con = sqlite3.connect("./gemaDB/gematriac.db")
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
    
    WORDMAP.clearRAM() #empty RAM

    #insert new word to SQL DB
    #check for duplicate words:
    cur.execute("select word from wordpool where word = :wordstr", {"wordstr":word})
    tmpWords = cur.fetchall()
    
    if tmpWords == []:
        cur.execute("insert into wordpool values (:wordstr)", {"wordstr": word})
        con.commit()
    
    #build tree
    wordpool = getWordsFromSQL()
    for i in wordpool:
        WORDMAP.addWord(i[0])
    
    #print tree
    WORDMAP.printMapping()

    return

def printDB():
    global con, cur
    
    WORDMAP.clearRAM() #empty RAM

    #load db to RAM
    wordpool = getWordsFromSQL()
    
    #build tree
    for i in wordpool:
        WORDMAP.addWord(i[0])
    
    #print tree
    WORDMAP.printMapping()

    return

def emptyDB():
    global cur,con
    cur.execute("delete from wordpool")
    con.commit()
    return

def closeDB():
    global con
    con.close()
