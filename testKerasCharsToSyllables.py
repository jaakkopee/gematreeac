import gemNumFuncs2 as gnf2
import NineRootedTreeWords as nrtw
import getwordsfromdbs as gwdb
import numpy as np
from keras.layers import LSTM, Dense
from keras.models import Sequential, load_model
import random
import sys
import nltk
from nltk.tokenize import SyllableTokenizer

def extract_syllables(word):
    syllable_tokenizer = SyllableTokenizer()
    syllables = syllable_tokenizer.tokenize(word)
    return syllables

textbase = open("kalevalaEngRuno9.txt", "r").read()
textbase = textbase.lower()
for i in textbase:
    if not i.isalnum():
        textbase=textbase.replace(i, " ")

words = textbase.split()
#words = gwdb.getDeepMem() 
charsAndSyls=[]
allSyllables=[]
for i in range(len(words)-1):
    charGVs=[gnf2.getGematria(char, "ScaExt") for char in words[i]]
    syllables = extract_syllables(words[i+1])
    allSyllables.extend(syllables)
    syllableGVs=[gnf2.getGematria(syl, "ScaExt") for syl in syllables]
    charsAndSyls+=[(charGVs, syllableGVs)]

maxCharGV = float(max([i for i in charGVs]))
maxSylGV = float(max([i for i in syllableGVs]))

print (charsAndSyls)
chrArray=[]
sylArray=[]
for i in charsAndSyls:
    chrArray+=[i[0]]
    sylArray+=[i[1]]

max_length_chars = max([len(i) for i in chrArray])
max_length_syls = max([len(i) for i in sylArray])

inArray=np.zeros((len(chrArray), max_length_chars), dtype=np.float32)
outArray=np.zeros((len(chrArray), max_length_chars), dtype=np.float32)


for i in range(len(chrArray)):
    for j in range(len(chrArray[i])):
        inArray[i][j]=float(chrArray[i][j])/maxCharGV
        if i < len(sylArray):
            if j < len(sylArray[i]):
                outArray[i][j]=float(sylArray[i][j])/maxSylGV

print("Numpy Arrays:")
print(inArray, outArray)

inArray=inArray.reshape(len(inArray), len(inArray[0]), 1)
outArray=outArray.reshape(len(outArray), len(outArray[0]), 1)
print (inArray.shape)
print (outArray.shape)

"""
model = Sequential()
model.add(LSTM(128))
model.add(Dense((max_length_chars), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(inArray, outArray, batch_size=64, epochs=128)

model.save("./gematriaLSTM")
"""
#for i in gwdb.getDeepMem():
#    allSyllables.extend(extract_syllables(i))

tree = nrtw.NineRootedTree(list(dict.fromkeys(allSyllables)), "ScaExt")

model = load_model("./gematriaLSTM")

seed = sys.argv[1]

print("Prediction")
inputChars = np.zeros(inArray[0].shape, dtype=np.float32)


words = [i for i in seed]
chars = [i for i in words]
charGVs = [gnf2.getGematria(i, "ScaExt") for i in chars]

maxNewCharGVs = max(charGVs)

for i in range(len(charGVs)-1):
    inputChars[i]=float(charGVs[i])/float(maxNewCharGVs)


result = model.predict(inputChars)

sylGVs = []
for i in result[0]:
    sylGVs+=[i]


for i in range(len(sylGVs)):
    sylGVs[i] = int(round(sylGVs[i]*maxSylGV))

endSentence = ""

for i in sylGVs:
    syls = tree.findWords(i)
    if not syls == []:
        endSentence+=random.choice(syls)

print (sylGVs)
print (endSentence)
