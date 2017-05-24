#DiceSim
#Written by Dylan Webb on 2.8.17

import random

faceNum = int(input("Enter the number of faces your die has: "))

if faceNum > 0 :
    
    #dice setup
    die = [int]*faceNum
    i = 0
    while i < faceNum :
        die[i] = i+1
        i+=1
    
    rollNum = int(input("Enter the number of dice you would like to roll: "))
    
    #perform random rolls
    diceRes = [int]*rollNum
    k = 0
    while k < rollNum :
        diceRes[k] = die[int(random.uniform(0,faceNum))]
        k += 1
    
    #print results
    print(diceRes)
    if rollNum > 1 :
        print("Sum =", sum(diceRes))
        if faceNum > 1 :
            print("Average =", sum(diceRes)/float(rollNum))
        
else :
    print("This program can't roll imaginary dice")
