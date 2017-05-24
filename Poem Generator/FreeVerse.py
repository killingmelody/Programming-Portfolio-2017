wordBank = ["inspecting","tutelage","raven","fiery","cricket","traversing",\
            "baby turtle","skipping","slippery","hate","love","cent","fuel",\
            "shrill","macho","substantial","question","cut","jogging","cherry",\
            "youthful","lethal","letters","can","and","not","with","beneath",\
            "the","but","woman","garrulous","suspending","noiseless","veil",\
            "orange","kitty cat","seventeen","merengue","semi-truck","poverty",\
            "workable","onerous","ajar","jarring","lioness","rocket",\
            "black holes","if","when","sudden","unsettling","roaring","wafting"]

import random
from PoemGenerator import PoemGenerator

class FreeVerse(PoemGenerator):

    def __init__(self):
        print("\nLet's build a free verse poem on your fridge!\n")
        randWords = list()

    def chooseRand(self):
        num = int(input("How many random words do you want off of the fridge? \
(between 1 and 10): "))

        if num < 11 and num > 0 :
            self.randWords = random.sample(wordBank, k=num)
        else :
            print("You have entered an incorrect number of words")

    def writePoem(self):
        finList = self.randWords + self.wordList
        finList = random.sample(finList, len(finList))

        #separate the list into groups of four and add spaces
        i = 0
        while i < len(finList) :
            if i%4 == 3 :
                finList[i] += "\n"
            else :
                finList[i] += " "
            i+=1
            
        finString = "".join(finList)
        
        print("\n" + self.title + "\n\n" + finString)
