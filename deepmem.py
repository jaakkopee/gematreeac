import sqlite3
from ndigitsets3 import getGematria

conDM = sqlite3.connect("./gemaDB/deepmem.db")
curDM = conDM.cursor()

curDM.execute("create table if not exists wordpool (word text)")
conDM.commit()

def addWordToDeepMem(word):
    global curDM,conDM

    #insert new word to SQL DB
    #check for duplicate words:
    curDM.execute("select word from wordpool where word = :wordstr", {"wordstr":word})
    tmpWords = curDM.fetchall()
    
    if tmpWords == []:
        curDM.execute("insert into wordpool values (:wordstr)", {"wordstr": word})
        conDM.commit()

    return

def getWordsFromDeepMem():
    global conDM, curDM
        
    curDM.execute("select * from wordpool")
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

