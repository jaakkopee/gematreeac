import gemNumFuncs2 as gnf2
import NineRootedTree4 as nrt4

import numpy as np
from keras.layers import LSTM, Dense
from keras.models import Sequential

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

charsAndSyls=[]
allSyllables=[]
for i in range(len(words)-1):
    charGVs=[gnf2.getGematria(char, "ScaExt") for char in words[i]]
    syllables = extract_syllables(words[i+1])
    allSyllables.extend(syllables)
    syllableGVs=[gnf2.getGematria(syl, "ScaExt") for syl in syllables]
    charsAndSyls+=[(charGVs, syllableGVs)]

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
        inArray[i][j]=float(chrArray[i][j])
        if i < len(sylArray):
            if j < len(sylArray[i]):
                outArray[i][j]=float(sylArray[i][j])

print("Numpy Arrays:")
print(inArray, outArray)

inArray=inArray.reshape(len(inArray), len(inArray[0]), 1)
outArray=outArray.reshape(len(outArray), len(outArray[0]), 1)
print (inArray.shape)
print (outArray.shape)

model = Sequential()
model.add(LSTM(128))
model.add(Dense((max_length_chars), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(inArray, outArray, batch_size=64, epochs=100)
import sys
print("Prediction")
inputChars = np.zeros(inArray[0].shape, dtype=np.float32)
sentence = sys.argv[1]
words = [i for i in sentence]
chars = [i for i in words]
charGVs = [gnf2.getGematria(i, "ScaExt") for i in chars]

for i in range(len(charGVs)):
    inputChars[i]=charGVs[i]

result = model.predict(inputChars)
import random
import NineRootedTree4 as nrt4

print(result)
resultSyllableGVs=[]
for i in range(len(result)):
    resultSyllableGVs+=[result[i]]

for i in range(len(resultSyllableGVs)):
    for j in range(len(resultSyllableGVs[i])):
        resultSyllableGVs[i][j]=int(round(resultSyllableGVs[i][j]*1024))
print(resultSyllableGVs)
tree = nrt4.syllableList_to_NineRootedTree(list(dict.fromkeys(allSyllables)), "ScaExt")
print(tree)

endSentence = ""
for i in resultSyllableGVs:
    for j in i:
        endSentence+=random.choice(tree.findSyllables(j))

print(endSentence)

