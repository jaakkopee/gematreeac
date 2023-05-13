import gemNumFuncs as gnf
import getwordsfromdbs as gwdb
from rich.tree import Tree
from rich import print

class Word:
  def __init__(self, value):
    self.value = value
    self.children = {}
    self.words = []
    return

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
      if not word in parent.words:
        parent.words+=[word]
      return word

    def findWords(self, value):
      if value == 0:
        return []
        
      route = gnf.getParentList(value)
      route.reverse()

      node = self.roots[route[0]]
      if value == node.value:
        return node.words

      for i in route[1:]:
        node = node.children.get(i)
        if node != None:
          if i == value:
            return node.words
      return []



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
    
    global globalColorTree
    globalColorTree = Tree("[red]NineRootedTree")

    def iterRoots(self, colorTree=None):
        colorTree = globalColorTree if colorTree is None else colorTree
        for root in self.roots:
          if root is not None:
            newColorTree = colorTree.add("[blue]"+str(root.value) + "[magenta]"+str(root.words))
            self.iterChildren(root, newColorTree)
           
        return globalColorTree
    
    def iterChildren(self, word, colorTree):
        for child in word.children.values():
            newColorTree = colorTree.add("[blue]"+str(child.value) + "[magenta]"+str(child.words))
            self.iterChildren(child, newColorTree)
        return globalColorTree
    
    def tree_in_color(self):
        return self.iterRoots()
    
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

