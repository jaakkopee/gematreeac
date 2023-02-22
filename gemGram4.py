from collections import defaultdict
from itertools import product
import getwordsfromdbs as gwdb
from gemNumFuncs_old import getGematria
import pyphen
import sys

def calculateGematria(word):
    return getGematria(word, "ScaExt")

def find_matching_syllables(syllables, gematria_value):
    matching_syllables = defaultdict(list)
    for syllable in syllables:
        value = calculateGematria(syllable)
        matching_syllables[value].append(syllable)
    return matching_syllables[gematria_value]

def generate_matching_words(syllables, words):
    matching_words = []
    for word in words:
        word_syllables = extract_syllables(word)
        possible_matching_syllables = [
            find_matching_syllables(syllables, calculateGematria(word_syllable))
            for word_syllable in word_syllables
        ]
        for matching_word_syllables in product(*possible_matching_syllables):
            matching_word = ''.join(matching_word_syllables)
            if calculateGematria(matching_word) == calculateGematria(word):
                matching_words.append(matching_word)
    return matching_words

def extract_syllables(words):
    dic = pyphen.Pyphen(lang='en_US')
    syllables=[]
    for word in words:
        syllables += dic.inserted(word.lower()).split('-')
    return syllables

words = gwdb.getDeepMem()
syllables = extract_syllables(words)

print(generate_matching_words(syllables, sys.argv[1]))
