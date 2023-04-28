# Insertion Sort Ascending

def insertionSortA(theList):
    for index in range (1, len(theList)):
        temp = theList [index]
        position = index
        while position > 0 and temp < theList[position-1]:
            theList[position] = theList[position-1]
            position = position-1
        theList[position] = temp
    return(theList)

marks = [23,45,23,56,78,56,45,23,45,12]
order = insertionSortA(marks)
print(order)