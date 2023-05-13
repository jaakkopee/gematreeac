import NineRootedTreeColourPrint as nrtcp
import rich

words=["alku", "loppu", "aika", "tarkkuus", "meno", "meininki", "yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän", "kymmenen", "ääretön"]
nrt = nrtcp.wordList_to_NineRootedTree(words, "ScaExt")
rich.print(nrt.tree_in_color())
