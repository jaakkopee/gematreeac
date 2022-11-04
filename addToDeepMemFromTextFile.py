import sqlite3 as sql
from tracemalloc import Snapshot
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

f = open("nimetBest.txt", "r")
data=" "
while data:
    data = f.readline()
    if not data:
        break

    sana=data

    for i in sana:
        if not i.isalpha():
            sana=sana.replace(i, "")

    sana=sana.lower()
    if len(sana)>0:
        addWordToDeepMemOuter(sana)

f.close()
        

conDM.close()
