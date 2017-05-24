#Small Number Puzzle
#Written by Dylan Webb on 3.16.17

import random
from OrderingProgram import Order

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#generate list of integers for puzzle
numPool = 9

intList = [int]*numPool
i = 0
while i < numPool :
    intList[i] = i+1
    i += 1

random.shuffle(intList)
intList = intList[0:4]
intString = str()
for int in intList :
    intString += str(int)

#clues
if intList[0] < intList[1] :
    print("The first integer is less that the second")
else :
    print("The first integer is greater that the second")

if intList[2]%2 == 0 :
    print("The third integer is even")
else :
    print("The third integer is odd")

print("The fourth integer minus the first is " + str(intList[3]-intList[0]))

print("Your numbers are: " + str(Order.orderIntegers(intList))) #order display

#user guesses password
password = ""
while password != intString :
    password = input("The password is: ")

    if password == intString :
        print("Correct!")
    else :
        print("Incorrect.")
        
input('\nPress ENTER to close')
