import sqlite3

from gemNumFuncs import getGematria
con = sqlite3.connect("./gematriac.db")

def getWordsFromSQLByNumber(number):
    cur = con.cursor()
    outList=[]
    cur.execute("select * from wordpool")
    data = cur.fetchall()
    for i in data:
        if getGematria(i[0])==number:
            outList+=[i[0]]
    return outList

def getWordsFromDeepMem():
    curDM = con.cursor()
    curDM.execute("select * from deepmem")
    data = curDM.fetchall()
    return data

def searchDeepMemByNumber(number):
    global conDM, curDM
    retList = []
    for i in getWordsFromDeepMem():
        gv = getGematria(i[0])
        if gv==number:
            retList+=[(i[0],gv)]
    return retList
