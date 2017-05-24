prepList = ["under","around","between","against","beneath","above","through",\
            "like","with","as","during","like","for","toward"]

advList = ["sloppily","frantically","joyfully","gleefully","morosely",\
           "insipidly","distinctly","bashfully","beautifully","bitterly",\
           "equally","exactly","continually","courageously"]

import random
from PoemGenerator import PoemGenerator

class SentenceForm(PoemGenerator):
    
    def __init__(self):
        print("\nLet's build a sentence on your fridge!\n")
        prep = adv = str()
        num = int()

    def chooseForm(self):

        self.num = int(input("Enter a value between 1 and 100: "))

        self.prep = prepList[int(random.uniform(0,len(prepList)))]
        self.adv = advList[int(random.uniform(0,len(advList)))]

    def writeSentence(self):
        formNum = 3;

        if self.num%formNum == 0 :
            print("\n" + self.title + "\n\n" + "The " + self.adj1 + self.n1 +\
                  "was " + self.v1 + self.prep + " a " + self.adj2 + self.n2 +\
                  ",\nWhen it began " + self.adv + " " + self.v2 + ".")
            
        if self.num%formNum == 1 :
            print("\n" + self.title + "\n\n" + "Once there was a " + self.adj1+\
                  self.n1 + ".\nIt started " + self.v1 + self.prep + " a " +\
                  self.adv + " " + self.v2 + self.n2 + ".\nThat was a " +\
                  self.adj2 + "day .")

        if self.num%formNum == 2 :
            print("\n" + self.title + "\n\n" + "The other day " + self.n1 +\
                  "saw a " + self.adj1 + ", " + self.adj2 + self.n2 + ".\n" +\
                  "Suddenly , the " + self.adj1 + ", "+ self.adj2 + self.n2 +\
                  "began\n" + self.v1 + self.adv + " " + self.prep + " " +\
                  self.n1 + ".\nThat was when " + self.n1 + "commenced " +\
                  self.v2 + ".")
