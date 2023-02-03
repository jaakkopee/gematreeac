import getwordsfromdbs as gwdb
import pyphen

def extract_syllables(words):
    dic = pyphen.Pyphen(lang='en_US')
    syllables=[]
    for word in words:
        syllables += dic.inserted(word.lower()).split('-')
    return syllables

words = gwdb.getDeepMem()
syllables = extract_syllables(words)


