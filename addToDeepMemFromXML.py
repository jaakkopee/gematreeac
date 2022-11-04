import xml.etree.ElementTree as ET
import sqlite3 as sql

tree = ET.parse('kotus-sanalista_v1.xml')
root = tree.getroot()

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

for i in root:
    sana = i[0].text
    for j in sana:
        if not j.isalpha():
            sana = sana.replace(j,"")
    sana=sana.lower()

    addWordToDeepMemOuter(sana)

conDM.close()

