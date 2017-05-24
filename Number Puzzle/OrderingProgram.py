#Ordering Program
#Written by Dylan Webb on 3.16.17

class Order :

    def init__self__(self) :
        pass

    def orderIntegers(intList) :
        j = 0
        while j < len(intList) :
            i = 0
            while i < len(intList)-1 :
                if intList[i] > intList[i+1] :
                    dummy = intList[i]
                    intList[i] = intList[i+1]
                    intList[i+1] = dummy
                i += 1
            j += 1
        
        return intList
