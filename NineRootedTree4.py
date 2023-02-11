import gemNumFuncs as gnf
import getwordsfromdbs as gwdb
from nltk.tokenize import SyllableTokenizer
syllable_tokenizer = SyllableTokenizer()
def extract_syllables(word_list):
  syllables=[]
  for word in word_list:
    word_syllables = syllable_tokenizer.tokenize(word)
    syllables.extend(word_syllables)
  return list(dict.fromkeys(syllables))

word_list = gwdb.getDeepMem()
syllables = extract_syllables(word_list)

def extract_syllables2(word):
  return syllable_tokenizer.tokenize(word)

class Syllable:
  def __init__(self, value):
    self.value = value
    self.children = {}
    self.syllables = []
    return
  

  def findSyllables(self, value):
    for i in list(self.children.values()):
      gemval = gnf.getGematria(i.syllables[0], "ScaExt")
      #print (str(gemval)+" "+str(value), end=" ")
      if gemval == value:
        return i.syllables
      
      else:
        for j in list(self.children.values()):
          syllables=j.findSyllables(value)
          if syllables:
            return syllables
          
          
class NineRootedTree:

    def __init__(self, syllables):
      self.roots = [None, None, None, None, None, None, None, None, None, None]
      for syllable in syllables:
        route = gnf.getParentList(gnf.getGematria(syllable, "ScaExt"))
        parent = self.roots[gnf.getRootNumber(route[0])]
        if parent is None:
          self.roots[gnf.getRootNumber(route[0])] = Syllable(gnf.getRootNumber(route[0]))
          self.roots[gnf.getRootNumber(route[0])].syllables.extend([i for i in syllables if gnf.getGematria(i, "ScaExt") == gnf.getGematria(syllable, "ScaExt")])
          parent = self.roots[gnf.getRootNumber(route[0])]
        route.reverse()
        for digit in route[1:]: 
          next = parent.children.get(digit)
          if next is None:
            next = Syllable(digit)
            #print("next.value:"+str(next.value))
            parent.children[digit] = next
            next.syllables+=[i for i in syllables if gnf.getGematria(i, "ScaExt") == digit]
          parent=next  
      return

    def findSyllables(self, value):
      for r in self.roots[1:]:
        #print("findSyllables:"+str(r.value)+" "+str(value))
        if value == r.value:
          return r.syllables
      for root in self.roots[1:]:
        #print ("calling recursive findSyllables, root value:"+str(root.value))
        syllables = root.findSyllables(value)
        if syllables:
          return syllables
        else:
          continue
        
    def route_to_root(self, syllable):
        return gnf.getParentList(gnf.getGematria(syllable, "ScaExt"))
                               
    def __str__(self):
        tree_str = ''
        for root in self.roots:
            if root is not None:
                tree_str += self.print_tree(root, '')
        return tree_str

    def print_tree(self, syllable, prefix):
        tree_str = prefix + str(syllable.value) + str(syllable.syllables) + '\n'
        prefix += '|  '
        for child in syllable.children.values():
            tree_str += self.print_tree(child, prefix)
        return tree_str

def list_to_NineRootedTree(syllables):
  tree = NineRootedTree(syllables)
  return tree

