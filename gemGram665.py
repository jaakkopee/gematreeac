import nltk
from nltk.tokenize import SyllableTokenizer
import getwordsfromdbs as gwdb
import gemNumFuncs_old as gnf
import random
import sys

def extract_syllables(word):
    syllable_tokenizer = SyllableTokenizer()
    return syllable_tokenizer.tokenize(word)

def calculate_gematria(syllable):
    return gnf.getGematria(syllable, "ScaExt")

def replace_syllables(word, syllable_list):
  syllables = extract_syllables(word)
  new_syllables = []
  for syllable in syllables:
    gematria_value = calculate_gematria(syllable)
    matching_syllables = [s for s in syllable_list if calculate_gematria(s) == gematria_value]
    new_syllables.append(random.choice(matching_syllables))
  return new_syllables

syllable_list=[]
for i in gwdb.getDeepMem():
    syllable_list += extract_syllables(i)

words = sys.argv[1].lower()
sentence = words.replace(" ", "")

print(words+" "+str(gnf.getGematria(sentence, "ScaExt"))+" => ")

new_syllables=[]
for i in words.split():
    new_syllables += [replace_syllables(i, syllable_list)]

new_word_str=""

for i in new_syllables:
    for j in i:
        new_word_str+=j
    new_word_str+=" "

new_sentence=new_word_str.replace(" ", "")

print (new_word_str+" "+str(gnf.getGematria(new_sentence, "ScaExt")))
