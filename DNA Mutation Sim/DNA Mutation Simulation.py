#DNA Mutation Simulation
#Written by Dylan Webb on 4.23.17

import random, string

alpha = list(string.ascii_uppercase)
mutNum = 0

length = int(input('Choose length of DNA between 2 and 26: '))

if length <= 26 and length >= 2:

    DNA = alpha[0:length]
    dummy = alpha[0:length]
    #prints DNA as a string
    print('\n' + ''.join(c for c in str(DNA) if c not in '[,]\''))

    mode = input('\nEnter D for diagnostic mode, or R for run mode: ')
    
    if mode == 'R':
        cycle = int(input('\nChoose number of cycles of replication: '))
        prob = 100 #probability of a mutation is one over this number
    elif mode == 'D':
        cycle = 1000000
        temp = input('\nEnter probability of mutation in the form of 1/n: ')
        prob = int(temp[2:])
    else:
        cycle = 0

    if cycle >= 1:
        
        print('\nReplicating...\n')

        #mutation loop
        i = 0
        while i < cycle and dummy == alpha[0:length] and DNA != []:
              
            ran = random.randint(1,prob)

            #applying mutations
            
            #deletion
            if ran == 1:
                num1 = random.randint(1,len(DNA))-1
                DNA.remove(DNA[num1])
            
            #insertion
            elif ran == 2:
                num1 = random.randint(1,len(DNA))-1
                num2 = random.randint(1,len(alpha))-1
                DNA.insert(num1,alpha[num2])
            
            #substitution
            elif ran == 3:
                num1 = random.randint(1,len(DNA))-1
                segLen = len(DNA) - num1
                len1 = random.randint(1,segLen)
                num2 = random.randint(len1,len(alpha))-1
                j = 0
                while j < len1:
                    DNA.remove(DNA[num1])
                    j += 1
                DNA.insert(num1,alpha[(num2-len1):num2])
                
            #inversion
            elif ran == 4:
                num1 = random.randint(1,len(DNA))-1
                segLen = len(DNA) - num1
                len1 = random.randint(1,segLen)-1
                seg1 = DNA[num1:num1+len1]
                seg2 = list(reversed(seg1))
                j = 0
                while j < len1:
                    DNA.remove(DNA[num1])
                    j += 1
                DNA.insert(num1,seg2)
                
            #duplication
            elif ran == 5:
                num1 = random.randint(1,len(DNA))-1
                segLen = len(DNA) - num1
                len1 = random.randint(1,segLen)-1
                seg1 = DNA[num1:num1+len1]
                DNA.insert(num1,seg1)

            else:
                mutNum -= 1

            if mode == 'D':
                dummy = DNA
                
            i += 1

        #output results
        print(' '.join(c for c in str(DNA) if c not in '[,]\' '))
        if mode == 'R':
            if DNA != []:
                print('\nNumber of mutations: ' + str(i+mutNum))
                print('(running at 1/100 probability of mutation)')
            else:
                print('\nDNA was completely removed by deletion mutations,')
        else:
            if i == cycle:
                print('\nNo mutation within 1,000,000 cycles')
            else:
                print('\nNumber of cycles to mutate: ' + str(i))
                print('Note--a benign mutation is possible')

#bounds on input
    else:
        if mode == 'R':
            print('That is not a valid number')
        else:
            print('That is not a valid mode')

else:
    print('That is not a valid length')

input('\nPress ENTER to close')
