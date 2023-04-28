def bubbleSortA(theList):
    swapped = True
    while swapped == True:
        swapped = False
        for index in range(1,len(theList)):
            if theList[index-1] > theList [index]:
                temp = theList[index-1]
                theList[index-1] = theList[index]
                theList[index] = temp
                swapped = True
    return(theList)

marks = [23,56,47,87,26,54,32,8]
letters = ["D","F","R","W","G","K"]

orderedMarks = bubbleSortA(marks)
lettersInOrder = bubbleSortA(letters)

print (orderedMarks)
print(letters)






