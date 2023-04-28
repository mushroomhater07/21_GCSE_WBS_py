def uubA(thug):
    sw = True
    while sw == True:
        sw == False
        for index in range(1,len(thug)):
            if thug[index-1] > thug[index]:
                temp = thug[index-1]
                thug[index-1] = thug[index]
                thug[index] = temp
                sw = True
    return(thug)

marks = [86,67,39,44,92,37]

order = uubA(marks)

print(order)
