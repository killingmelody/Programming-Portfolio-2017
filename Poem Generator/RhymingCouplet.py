rhyme0 = ["make","take","lake","shake","rake","ache","fake","break","snake",\
          "bake","cake","stake","wake"]

rhyme1 = ["lie","dye","sigh","my","dry","fly","bye","rhye","guy","why",\
          "shy","pie","tie"]

rhyme2 = ["show","go","no","slow","flow","crow","bow","toe","dough","foe",\
          "mow","grow","glow","GI Joe"]

rhyme3 = ["chair","bear","tear","swear","mare","glare","bus fare","lair",\
          "snare","pear","dare"]

import random
from PoemGenerator import PoemGenerator

class RhymingCouplet(PoemGenerator):
    
    def __init__(self):
        print("\nLet's build a rhyming couplet on your fridge!\n")
        c1 = c2 = str()

    def chooseRhyme(self):
        rhymeNum = 4

        val = int(input("Enter a value between 1 and 100: "))
        
        if val%rhymeNum == 0 : #rhyme list 0
            rhymeDummy = rhyme0

        if val%rhymeNum == 1: #rhyme list 1
            rhymeDummy = rhyme1

        if val%rhymeNum == 2: #rhyme list 2
            rhymeDummy = rhyme2

        if val%rhymeNum == 3: #rhyme list 3
            rhymeDummy = rhyme3
            
        couplet1 = rhymeDummy[int(random.uniform(0,len(rhymeDummy)))]
        couplet2 = rhymeDummy[int(random.uniform(0,len(rhymeDummy)))]

        #removes repetition
        i = 0
        while i < 10 :
            if couplet1 == couplet2 :
                couplet2 = rhymeDummy[int(random.uniform(0,len(rhymeDummy)))]
            i+=1

        self.c1 = couplet1
        self.c2 = couplet2

    def writePoem(self):
        print("\n" + self.title + "\n\n" + "The " + self.adj1 + self.n1 + \
            "was " + self.v1 + "by a " + self.c1 + ",\n" + "When " + "the"  + \
            self.n2 + "began " + self.v2 + "a " + self.adj2 + self.c2 + ".")
