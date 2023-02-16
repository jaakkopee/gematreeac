import gemNumFuncs as gnf
import getwordsfromdbs as gwdb

class Word:
  def __init__(self, value):
    self.value = value
    self.children = {}
    self.words = []
    return
  

  def findWords(self, value, cipher):
    if value == 0:
      return [""]

    for i in list(self.children.values()):
      gemval = gnf.getGematria(i.words[0], cipher)
      #print (str(gemval)+" "+str(value), end=" ")
      if gemval == value:
        return i
      
      else:
        for j in list(self.children.values()):
          words=j.findWords(value, cipher)
          if words:
            return words
        
      return ["?"]
          
class NineRootedTree:

    def __init__(self, words, cipher):
      self.roots = [None, None, None, None, None, None, None, None, None, None]
      if words:
        for i in words:
          self.addWord(i, cipher)        
      return

    def addWord(self, word, cipher):
      route = gnf.getParentList(gnf.getGematria(word, cipher))
      route.reverse()
      parent = self.roots[route[0]]
      if parent is None:
        self.roots[route[0]] = Word(route[0])
        parent = self.roots[route[0]]
      for digit in route[1:]: 
        next = parent.children.get(digit)
        if next is None:
          next = Word(digit)
          parent.children[digit] = next
        parent=next  
      parent.words+=[word]
      return


    def findWords(self, value):
      for r in self.roots[1:]:
        #print("findWords:"+str(r.value)+" "+str(value))
        if value == r.value:
          return r.words
      for root in self.roots[1:]:
        #print ("calling recursive findWords, root value:"+str(root.value))
        words = root.findWords(value, "ScaExt")
        if words:
          return words
        else:
          continue
        
    def route_to_root(self, word, cipher):
        return gnf.getParentList(gnf.getGematria(word, cipher))
                               
    def __str__(self):
        tree_str = ''
        for root in self.roots:
            if root is not None:
                tree_str += self.print_tree(root, '')
        return tree_str

    def print_tree(self, word, prefix):
        tree_str = prefix + str(word.value) + str(word.words) + '\n'
        prefix += '|  '
        for child in word.children.values():
            tree_str += self.print_tree(child, prefix)
        return tree_str

    def generateNestedList(self):
        result = "<ul>"
        for root in self.roots:
          if root is not None:
            result+=self.generateListItems(root)
        result+="</ul>"
        return result

    def generateListItems(self, word):
      result = "<li>" + str(word.value) + "<div>"+str(word.words)+"</div></li>"
      if word.children:
          result += "<ul>"
          for child in word.children.values():
              result += self.generateListItems(child)
          result += "</ul>"
      return result


def wordList_to_NineRootedTree(words, cipher):
  tree = NineRootedTree(words, cipher)
  return tree

