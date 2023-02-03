import random
import getwordsfromdbs as gwdb
import sys
from termcolor import colored, COLORS

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

def buildGematriaDictionary(wordlist):
    gematria_dict = {}
    for word in wordlist:
        gematria = calculateGematria(word)
        if gematria in gematria_dict:
            gematria_dict[gematria].append(word)
        else:
            gematria_dict[gematria] = [word]
    return gematria_dict

def transformText(text, gematria_dict):
    transformed_text = ""
    words = text.split()
    for word in words:
        gematria = calculateGematria(word)
        if gematria in gematria_dict:
            replacement_word = random.choice(gematria_dict[gematria])
            transformed_text += replacement_word + " "
        else:
            transformed_text += word + " "
    return transformed_text

wordlist = gwdb.getDeepMem() 
gematria_dict = buildGematriaDictionary(wordlist)

if len(sys.argv)>1:
    text = sys.argv[1]
else:
    text = "testisana"

if len(sys.argv)>2:
    iter = int(sys.argv[2])
else:
    iter = 1

print("Transforming sentence: "+text)


for i in range(iter):
    transformed_text = transformText(text, gematria_dict)
    print(colored(transformed_text, "red"))

