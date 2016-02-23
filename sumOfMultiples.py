#sum of multiples in python

def addMultiples(multiple, limit):
    nextMultiple = 0
    runSum = 0
    #if(multiple>limit):
        #print("multiple %d is greater than limit %d and therefore there can be no multiples")
        #break

    while nextMultiple < limit:
        nextMultiple = nextMultiple + multiple
        print(nextMultiple)
        if nextMultiple< limit:
            runSum = runSum + nextMultiple
        #print(runSum)
    return runSum

print (addMultiples(3, 10))
