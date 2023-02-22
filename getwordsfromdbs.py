import sqlite3

from gemNumFuncs_old import getGematria, getDistance

def searchWordListByDistance(word, wordList, currentCipher, closenessWeight = 1.0, maxDistance = 1.0):
    
    outputArray=[]
    for i in wordList:
        distance = getDistance(word, i, currentCipher, closenessWeight)
        if distance < maxDistance and i not in outputArray:
            outputArray+=[(i, getGematria(i, currentCipher))]


    return outputArray

def getDeepMem():
    con=sqlite3.connect("./gematriac.db")
    cur=con.cursor() 
    cur.execute("select * from deepmem order by word")
    data = cur.fetchall()
    con.close()
    outArray = []
    for i in data:
        outArray += [i[0]]
    
    return outArray

def searchDeepMemByDistance(word, currentCipher, closenessWeight=1.0, maxDistance = 1.0):
    con=sqlite3.connect("./gematriac.db")
    cur=con.cursor() 
    cur.execute("select * from deepmem order by word")
    data = cur.fetchall()
    con.close()
    
    outputArray=[]
    for i in data:
        distance = getDistance(word, i[0], currentCipher, closenessWeight)
        if distance < maxDistance and i not in outputArray:
            if not getGematria(word, currentCipher) == getGematria(i[0], currentCipher):
                outputArray+=[(i[0], getGematria(i[0], currentCipher))]


    return outputArray

def addWordToDeepMem(word):
    conDM=sqlite3.connect("./gematriac.db")
    curDM=conDM.cursor()
    #insert new word to SQL DB
    #check for duplicate words:
    curDM.execute("select word from deepmem where word = :wordstr", {"wordstr":word})
    tmpWords = curDM.fetchall()
    
    if tmpWords == []:
        curDM.execute("insert into deepmem values (:wordstr)", {"wordstr": word})
        conDM.commit()
        return True

    return False

def getWordsFromSQLByNumber(number):
    con = sqlite3.connect("./gematriac.db")
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
    con = sqlite3.connect("./gematriac.db")
    curDM = con.cursor()
    curDM.execute("select * from deepmem order by word")
    data = curDM.fetchall()
    con.close()

    return data

def searchDeepMemByNumber(number):
    retList = []
    for i in getWordsFromDeepMem():
        #i[0].replace("2","")
        gv = getGematria(i[0])
        if gv==number:
            retList+=[(i[0],gv)]
    retListFmtdStr=""
    for i in retList:
        retListFmtdStr+=str(i[0])+" "+str(i[1])+"\n"

    return retListFmtdStr

def searchDeepMemByNumberArray(number, currentCipher):
    retList = []
    for i in getWordsFromDeepMem():
        #i[0].replace("2","")
        gv = getGematria(i[0], currentCipher)
        if gv==number:
            retList+=[(i[0],gv)]

    return retList

def getWordValuePairs():
    con = sqlite3.connect("./gematriac.db")
    cur = con.cursor()
    cur.execute("select * from wordpool")
    data = cur.fetchall()
    #laske gematria ja talleta sanat ja luvut johki kätevään tietorakenteeseen
    outdata=[]
    for i in data:
        word = i[0]
        number = getGematria(i[0]) 
        outdata+= [(word, number)]

    con.close()

    return outdata

def deleteWordFromDeepMem(word):
    conDM=sqlite3.connect("./gematriac.db")
    cur = conDM.cursor()
    cur.execute("delete from deepmem where word="+word)
    conDM.commit()

def deleteDeepMem():
    conDM=sqlite3.connect("./gematriac.db")
    cur = conDM.cursor()
    cur.execute("delete from deepmem")
    conDM.commit()

  