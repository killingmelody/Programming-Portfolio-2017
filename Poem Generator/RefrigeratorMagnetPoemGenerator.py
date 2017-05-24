#Refrigerator Magnet Poem Generator
#Written by Dylan Webb on 3.6.17

from PoemGenerator import PoemGenerator
from RhymingCouplet import RhymingCouplet
from SentenceForm import SentenceForm
from FreeVerse import FreeVerse

print("Welcome to the Refrigerator Magnet Poem Generator")
pType = int(input("1. Rhyming Couplet\n2. Free Verse\n3. Sentence Form\n\
Enter the number corresponding to your poem type: "))

if pType == 1 :
    poem = RhymingCouplet()
    poem.chooseRhyme()
    poem.getWords()
    poem.title()
    poem.writePoem()

elif pType == 2 :
    poem = FreeVerse()
    poem.chooseRand()
    poem.getWords()
    poem.title()
    poem.writePoem()

elif pType == 3 :
    sentence = SentenceForm()
    sentence.chooseForm()
    sentence.getWords()
    sentence.title()
    sentence.writeSentence()

else :
    print("You have entered an incorrect Poem Type")
