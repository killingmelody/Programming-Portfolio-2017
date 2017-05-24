#99 bottles code
#Written by Dylan Webb on 1.23.17

i = 99
while i > 0:
    if i == 1 :
        print(i, "bottle of an undefined beverage on the wall")
        print(i, "bottle of an undefined beverage")
    else :
        print(i, "bottles of an undefined beverage on the wall")
        print(i, "bottles of an undefined beverage")
    print("Take one down & pass it around")
    i -= 1
    if i == 1 :
        print(i, "bottle of an undefined beverage on the wall\n")
    else :
        print(i, "bottles of an undefined beverage on the wall\n")
