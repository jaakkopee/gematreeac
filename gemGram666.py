from typing import List
from gemNumFuncs import getGematria
import getwordsfromdbs as gwdb
import pyphen
import sys

def generate_identical_gematria_words(original_words: List[str], syllables: List[str]):
    def calculate_gematria(word):
        return getGematria(word, "ScaExt")

    identical_gematria_words = []
    for word in original_words:
        original_gematria = calculate_gematria(word)
        for syllable in syllables:
            if calculate_gematria(syllable) == original_gematria:
                identical_gematria_words.append(syllable)
                break

    ret=""

    for word in identical_gematria_words:
        ret += word+" "+str(getGematria(word, "ScaExt"))+" "
        
    return ret

def extract_syllables(words):
    dic = pyphen.Pyphen(lang='en_US')
    syllables=[]
    for word in words:
        syllables += dic.inserted(word.lower()).split('-')
    return syllables

print(generate_identical_gematria_words(sys.argv[1].split(), extract_syllables(gwdb.getDeepMem())))
