from math import trunc
import sqlite3
from gemNumFuncs import getGematria

conDM = sqlite3.connect("./gematriac.db")
curDM = conDM.cursor()

curDM.execute("create table if not exists deepmem (word text)")
conDM.commit()
#change
def addWordToDeepMem(word):
    global curDM,conDM

    #insert new word to SQL DB
    #check for duplicate words:
    curDM.execute("select word from deepmem where word = :wordstr", {"wordstr":word})
    tmpWords = curDM.fetchall()
    
    if tmpWords == []:
        curDM.execute("insert into deepmem values (:wordstr)", {"wordstr": word})
        conDM.commit()
        return True

    return False

def getWordsFromDeepMem():
    global conDM, curDM
        
    curDM.execute("select * from deepmem")
    data = curDM.fetchall()
    return data

def searchDeepMemByNumber(number):
    retList = []
    for i in getWordsFromDeepMem():
        gv = getGematria(i[0])
        if gv==number:
            retList+=[(i[0],gv)]
    return retList

    return

def deleteWordFromDeepMem(word):
    global conDM
    cur= conDM.cursor()
    cur.execute("delete from deepmem where word="+word)
    conDM.commit()

def deleteDeepMem():
    global conDM
    cur = conDM.cursor()
    cur.execute("delete from deepmem")
    conDM.commit()
