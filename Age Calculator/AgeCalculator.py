#AgeCalculator
#Made by Dylan Webb on 2.2.17

import time;
tm = time.localtime(time.time())

birthday = input("Input your birthday as YYYY/MM/DD: ")
if len(birthday) == 10 :
    
    dAge = tm[2] - int(birthday[8:10])
    mAge = tm[1] - int(birthday[5:7])
    yAge = tm[0] - int(birthday[0:4])
    
    if dAge < 0 : #if current day is smaller than birthday, a month is subtracted and the days are added
        if (tm[1]-1) % 2 == 1 : #checks if the previous month is an odd # month
            dAge += 31
        elif (tm[1]-1) == 2 : #checks if the previous month is February
            if tm[0] % 4 == 0 :
                dAge += 29
            else :
                dAge += 28
        else: #checks if previous month was an even # month and not February
            dAge+=30
        mAge -= 1
        
    if mAge < 0 : #if current month is smaller than birthmonth, a year is subtracted and 12 months are added
        mAge += 12
        yAge -= 1
        
    print("You are " + str(yAge) + " years, " + str(mAge) + " months, and " + str(dAge) + " days old")
    
else :
    print("You have entered an incorrect number of characters")
