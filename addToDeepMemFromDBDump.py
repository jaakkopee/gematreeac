import sqlite3 as sql
conDM=sql.connect("./gematriac.db")
curDM=conDM.cursor()

def addWordToDeepMemOuter(word):   
    global curDM,conDM 
    curDM.execute("select word from deepmem where word = :wordstr", {"wordstr":word})
    tmpWords = curDM.fetchall()
    
    if tmpWords == []:
        curDM.execute("insert into deepmem values (:wordstr)", {"wordstr": word})
        conDM.commit()
        return True

    return False

def moveLoop(file):
    f = open(file, "r")
    data=True
    while data:
        data = f.readline()
        if not data:
            break
        
        sana = data.split()[0]
        for i in sana:
            if not i.isalpha():
                sana=sana.replace(i, "")
        sana=sana.lower()
        if len(sana)>0:
            addWordToDeepMemOuter(sana)

    f.close()

def moveLoop2(file):
    f = open(file, "r")
    data=True
    while data:
        data = f.readline()
        if not data:
            break
        
        sana = data.split("%")[0]
        for i in sana:
            if not i.isalpha():
                sana=sana.replace(i, "")
        sana=sana.lower()
        if len(sana)>0:
            addWordToDeepMemOuter(sana)

    f.close()

moveLoop("index.adj")   
moveLoop("index.adv")
moveLoop("index.noun")
moveLoop("index.verb")
moveLoop2("index.sense")

conDM.close()
