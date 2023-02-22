import random
import re
import getwordsfromdbs as gwdb
import sys
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import cmudict
from gemNumFuncs_old import getGematria
import pyphen

def calculateGematria(word, cipher="English extended"):
    # Dictionary of letter to numerical value mappings
    if cipher == "English extended":
        values = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'o': 60,
            'p': 70, 'q': 80, 'r': 90, 's': 100, 't': 200, 'u': 300, 'v': 400,
            'w': 500, 'x': 600, 'y': 700, 'z': 800
        }
    else:
        # Add other ciphers here as necessary
        raise ValueError("Unsupported cipher")

    # Calculate the gematria value by summing the values of each letter
    value = 0
    for letter in word:
        value += values.get(letter.lower(), 0)

    return value

def buildGematriaDictionary(syllablelist):
    gematria_dict = {}
    for syllable in syllablelist:
        syllable = syllable.lower()
        gematria = calculateGematria(syllable)
        if gematria in gematria_dict:
                gematria_dict[gematria].append(syllable)
        else:
            gematria_dict[gematria] = [syllable]

    return gematria_dict


def extract_syllables(words):
    dic = pyphen.Pyphen(lang='en_US')
    syllables=[]
    for word in words:
        syllables += dic.inserted(word.lower()).split('-')
    return syllables


def transformText(text, gematria_dict):
    transformed_text = ""
    words = text.split()
    for word in words:
        syllables = extract_syllables(word)
        transformed_word = ""
        for syllable in syllables:
            gematria = calculateGematria(syllable)
            if gematria in gematria_dict:
                replacement_syllable = random.choice(gematria_dict[gematria])
                transformed_word += replacement_syllable
            else:
                transformed_word += syllable
        transformed_text += transformed_word + " "
    return transformed_text

wordList=gwdb.getDeepMem()
print("creating syllable list")
syllablelist = extract_syllables(wordList)
syllablelist=list(dict.fromkeys(syllablelist))
print(syllablelist)

print("building dictionary")
gematria_dict = buildGematriaDictionary(syllablelist)
print (gematria_dict)

text = sys.argv[1]
iter = int(sys.argv[2])

print ("Transforming "+text+ " " + str([getGematria(j, "ScaExt") for j in text.split()]))

for i in range(iter):
    print ("iter:"+str(i))
    transformed_text = transformText(text, gematria_dict)
    print(transformed_text + " " + str([getGematria(j, "ScaExt") for j in transformed_text.split()]))

