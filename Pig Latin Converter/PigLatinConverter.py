#PigLatinConverter
#Written by Dylan Webb on 1.27.17

vowels = "aeiouAEIOU"

firstName = input('Type your first name and hit enter: ')
lastName = input('Do the same for your last name: ')

if firstName[0] in vowels : #check for starting vowel in first name
    firstName += "way"
else:
    firstName = firstName[1:] + firstName[0] + "ay"
    
if lastName[0] in vowels : #check for starting vowel in last name
    lastName += "way"
else:
    lastName = lastName[1:] + lastName[0] + "ay"

print("\nYour pig latin name is: " + firstName.capitalize() + ", " + lastName.capitalize())
