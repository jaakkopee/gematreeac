import sqlite3

from ndigitsets3 import getGematria

def getWordsFromSQLByNumber(number):
    con = sqlite3.connect("./gemaDB/gematriac.db")
    cur = con.cursor()
    outList=[]
    cur.execute("select * from wordpool")
    data = cur.fetchall()
    for i in data:
        if getGematria(i[0])==number:
            outList+=[i[0]]
    con.close()
    return outList

def getWordsFromDeepMem():
    conDM = sqlite3.connect("./gemaDB/deepmem.db")
    curDM = conDM.cursor()
    curDM.execute("select * from wordpool")
    data = curDM.fetchall()
    conDM.close()
    
    return data

def searchDeepMemByNumber(number):
    global conDM, curDM
    retList = []
    for i in getWordsFromDeepMem():
        gv = getGematria(i[0])
        if gv==number:
            retList+=[(i[0],gv)]
    return retList
