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

#deepMemAsList = gwdb.getDeepMem()
#deepMemSyllables = extract_syllables(deepMemAsList)

def extract_syllables2(word):
  return syllable_tokenizer.tokenize(word)

class Syllable:
  def __init__(self, value):
    self.value = value
    self.children = {}
    self.syllables = []
    return
  

  def findSyllables(self, value, cipher):
    for i in list(self.children.values()):
      gemval = gnf.getGematria(i.syllables[0], cipher)
      #print (str(gemval)+" "+str(value), end=" ")
      if gemval == value:
        return i.syllables
      
      else:
        for j in list(self.children.values()):
          syllables=j.findSyllables(value, cipher)
          if syllables:
            return syllables
        
      return [""]
          
class NineRootedTree:

    def __init__(self, syllables, cipher):
      self.roots = [None, None, None, None, None, None, None, None, None, None]
      for syllable in syllables:
        route = gnf.getParentList(gnf.getGematria(syllable, cipher))
        parent = self.roots[gnf.getRootNumber(route[0])]
        if parent is None:
          self.roots[gnf.getRootNumber(route[0])] = Syllable(gnf.getRootNumber(route[0]))
          self.roots[gnf.getRootNumber(route[0])].syllables.extend([i for i in syllables if gnf.getGematria(i, cipher) == gnf.getGematria(syllable, cipher)])
          parent = self.roots[gnf.getRootNumber(route[0])]
        route.reverse()
        for digit in route[1:]: 
          next = parent.children.get(digit)
          if next is None:
            next = Syllable(digit)
            #print("next.value:"+str(next.value))
            parent.children[digit] = next
            next.syllables+=[i for i in syllables if gnf.getGematria(i, cipher) == digit]
          parent=next  
      return

    def findSyllables(self, value):
      for r in self.roots[1:]:
        #print("findSyllables:"+str(r.value)+" "+str(value))
        if value == r.value:
          return r.syllables
      for root in self.roots[1:]:
        #print ("calling recursive findSyllables, root value:"+str(root.value))
        syllables = root.findSyllables(value, "ScaExt")
        if syllables:
          return syllables
        else:
          continue
        
    def route_to_root(self, syllable, cipher):
        return gnf.getParentList(gnf.getGematria(syllable, cipher))
                               
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

def syllableList_to_NineRootedTree(syllables, cipher):
  tree = NineRootedTree(syllables, cipher)
  return tree

