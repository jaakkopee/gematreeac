# GemaTreeAC 2=0
GemaTreeAC 2=0 is a gematria and numerology -based word classification algorithm and database. It is meant for searching meanings of words by mapping letters into numbers and comparing the values of words. Also numerological reduction is used to form a nine-rooted treestructure that has routes of numbers from leave to root. The code is a web application that is hosted at https://jpts.aprx.io

Gematria is the mapping of numbers (usually positive integers) with the letters of an alphabet. Gematria is used for searching associative meanings in words in the study of the Bible and the Torah, for example. I use it to construct words of power for my ritual work.

For classification of the numbers of selected words, GemaTreeAC utilizes a technique called numerological reduction. For example, the numbers 666 and 333 are seen as numerologically related. All numbers can be reduced numerologically into parent numbers. When numerological reduction is iterated until the resulting number is a single-digit number what we have is what I call the root number, that is, a number with a single digit (numbers 1 to 9). If the parent number is the same with two different numbers, they are seen as numerologically related.

The numerological reduction for numbers 666 and 333 is calculated as follows: 666 reduces to 6+6+6=18 and 18 reduces to 1+8=9. 333 reduces straight to 3+3+3=9. The numbers have the same root and are therefore related. The numbers have different routes to their root.

When numerological reduction is iterated multiple times, the numbers travel in a tree-like structure that has nine roots (numbers 1 to 9). Between the leaf numbers (666 and 333 in our example) and the root numbers (now only one, a common root: 9) it can be seen the numbers travel the tree from leaf to root on varying routes that converge as the number of digits in numbers decrease. The routes to root in my example are [666, 18, 9] and [333, 9].

To analyze this behavior I came up with the idea of n-digit sets. It is a grouping of values according to the number of digits in the numerical representations of values. The number 666 travels through n-digit sets n=3, n=2 to the set n=1. 333 travels straight from n=3 to n=1. The n-digit set n=1 has all the numbers, for every number has a root number. The higher the n in a given n-digit set, the smaller the probability of a certain number to appear in this set although the number of numbers in the set is greater. I’m not gifted enough in mathematics to formulate this phenomenon properly. The numbers go through n-digit sets in varying, interesting patterns.

There is a reason why, in kabbala, the low n-digit numbers are considered as powerful, even sacred. The amount of words related to a low n-digit number is higher than to a number with a higher number of digits. This means that by one special low n-digit word, a kabbalist can conjure up hundreds of meaningful associations (related words). Words with high amount of associations are called "words of power”. These words can be used in mantras, spells, prayers and prophecies.

All numbers and all words can be mapped to the tree of life, the main symbol of kabbalists. It is a composite symbol consisting of 11 sephiras and 22 paths. The sephiras represent the numbers 1 to 11 and the 22 paths represent the letters of the Hebrew alphabet. Numbers 10 and 11 are special. Number 10, representing matter, is viewed as the mirror of sephira 1, representing spirit. Number 11 is the number of the ”hidden” sephira that has special functions in the tree.

All numbers have occult meanings in the tree of life. Number nine is called ”The Foundation”. It represents sexuality, the astral and the subconscious. It’s planetary association is the moon. Number one (”The Crown”) represents consciousness. Numbers in set n=1 have very specific cognitive functions attributed to them. Higher-n numbers have more complex and also vague meanings as their meanings are composites of the meanings of numbers in set n=1. The higher the n, the more room is left for interpretation.

At the moment GemaTreeAC has only 8 ciphers that are used commonly in gematria study. I’d like to add more, hopefully original ciphers that work with gematria (produce lots of interesting associative meanings). I also want to develop and refine the data representation in GemaTreeAC. The nine-rooted tree is there already. The numbers are studied only by equivalence at the moment. I’d want to give the user tools for exploration of farther numerological relations. Via study of nwcp:s (numbers with common parents) other numerological relations can be explored.

ADDITION 18.12.2022:
[This date, the alpha.6 pre-release was packed up and the package has now a
GemaTreeAC that can do searches into numbers with common n-digit set, common root, common route to root, common number and a common word. This is due to
a distance measure which is calculated with a formula developed by me. Mathematics... gotta love it. gtac_math.pdf has a mathematical analysis of the Distance Measure Search algorithm. It is difficult to use, with it's 12 parameters and erratic behavior but I'm planning to make templates that will ease the search process. Also session memory is going to go through a reform
in the future to enable the use of these new numerological relationships in sentence formula and final sentence formulation.]

GemaTreeAC comes with database functionality and a read-only database called DeepMem of ca. 500000 words in Finnish, Swedish and English. DeepMem-database is gathered from kotus-sanalista_v1, WordNet 3.1, Gothenburg uni. Saldo 2.3 and Väestötietojärjestelmän Etunimitilasto

GemaTreeAC is a web application hosted at https://jpts.aprx.io .

For normal use, I recommend the online version. If you want to experiment with the code, you can download the latest release from https://github.com/jaakkopee/gematreeac/releases or clone the repository, and run your local version of GemaTreeAC.

To run GemaTreeAC locally, you need to have a http server on your computer. Python has a module, http.server, that will do for testing the code. Just install Python 3 from https://python.org and enter <pre>python3 -m http.server</pre> at the command line in your GemaTreeAC directory and point your browser to <pre>localhost:8000/GemaTreeAC_index.html</pre> 

Adding your own database to the Wizard Meditation / DeepMem -search is possible at https://jpts.aprx.io with the google chrome browser. Safari does not like local data, the last time I checked. Other browsers I haven't tested.

GemaTreeAC 2=0 is written in Python from https://python.org and PyScript from https://pyscript.net

GemaTreeAC is copylefted in 2022 by Jaakko Prättälä. All proprietary rights belong to the Great Spirit. Do What Thou Wilt with the code. Share the knowledge in the way you see as fit.

Feel free to contact me if you have questions, suggestions, feature requests or just want to talk about gematria/numerology/kabbala/occult stuff. I am a true numerology/gematria freak and a practicing mage.

--
Jaakko Prättälä
iipekaj@gmail.com

Sentence formula in action.
<img src="./IMG_7292.jpg"/>

A DMS Plot of the word 'suuripetotaivos' in the Fibonacci cipher. Parameters commonRoot and commonRoute are sought after. Also distance of gematria values is used to induce the
vortex like pattern in the plot. Other parameters are set to zero or close. Oh, and distanceBias is 1.0, too, if I recall correctly.
<img src="./suuripetotaivos66360.png"/>

